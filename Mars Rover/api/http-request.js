import axios from 'axios';
import { sanitizeUrl } from '@braintree/sanitize-url';
import filterXSS from 'xss';
import { getNestedObject } from 'utils/common';
let loadingTimer;

window.ajaxCallsCount = window.ajaxCallsCount || 0;

const showLoader = () => {
  const loader = document.querySelector('.loader');
  clearTimeout(loadingTimer);
  if (loader) {
    loader.classList.remove('hide');
  }
  window.ajaxCallsCount++;
};

const addHideClassToLoader = () => {
  const loader = document.querySelector('.loader');
  if (loader) {
    loader.classList.add('hide');
  }
};

/**
 * @description filter config
 * @param {object} object object to be filtered
 * @returns {object} XSS filtered object
 */
const filterXSSObject = (object) => {
  Object.keys(object).forEach((key) => {
    const value = object[key];
    const objectType = Object.prototype.toString.call(value);
    if (objectType === '[object Object]' || objectType === '[object Array]') {
      filterXSSObject(value);
    } else if (typeof value === 'string') {
      object[key] = filterXSS(value);
    }
  });
};

const hideLoading = () => {
  window.ajaxCallsCount--; // decrement this global variable when ajax req is complete
  if (window.ajaxCallsCount === 0) {
    // hide loader only if all active ajax requests are done
    loadingTimer = setTimeout(addHideClassToLoader, 200);
  }
};

const httpRequest = (
  config,
  extraHeaders,
  showGlobalLoader = true,
  preventHidingLoader = false
) => {
  if (showGlobalLoader) {
    showLoader();
  }
  const defaultConfig = {
    withCredentials: true,
    headers: {
      'Content-Type': 'application/json',
      'Cache-Control': 'no-cache',
      ...extraHeaders,
    },
  };

  let url;
  if (
    config.url.includes('authenticate') ||
    config.url.includes('lastLoginTimestamp') ||
    config.url.includes('devices')
  ) {
    url = `${process.env.REACT_APP_AUTH_API_ENDPOINT}${config.url}`;
  } else if (config.url.includes('access_token')) {
    url = `${process.env.REACT_APP_AUTHORIZE_API_ENDPOINT}${config.url}`;
  } else if (config.url.includes('revoke')) {
    url = `${process.env.REACT_APP_AUTHORIZE_REVOKE_API_ENDPOINT}${config.url}`;
  } else if (config.url.includes('endSession')) {
    url = `${process.env.REACT_APP_AUTHORIZE_END_SESSION_API_ENDPOINT}${config.url}`;
  } else if (config.useDirectUrl) {
    url = `${config.url}`;
  } else if (config.url.includes('sessions?_action=getSessionInfo')) {
    url = `${process.env.REACT_APP_SESSION_API_ENDPOINT}${config.url}`;
  } else if (config.url.includes('amazonaws')) {
    url = `${process.env.REACT_APP_COGNITO_ENDPOINT}`;
  } else if (config.url.includes('hyprAuth')) {
    url = `${process.env.REACT_APP_HYPER_AUTHENTICATION_ENDPOINT}`;
  } else if (config.url.includes('hypr')) {
    url = `${process.env.REACT_APP_HYPER_ENDPOINT}`;
  } else {
    url = `${process.env.REACT_APP_API_ENDPOINT}${config.url}`;
  }

  url = sanitizeUrl(url);
  filterXSSObject(config);
  const mergedConfig = {
    ...defaultConfig,
    ...config,
    url,
  };

  return axios(mergedConfig)
    .then((res) => {
      filterXSSObject(res);
      if (showGlobalLoader) {
        if (!preventHidingLoader) {
          hideLoading();
        } else {
          window.ajaxCallsCount--;
        }
      }
      return res;
    })
    .catch((error) => {
      if (showGlobalLoader) {
        hideLoading();
      }
      if (
        getNestedObject(error, ['response', 'data', 'code']) === 401 &&
        getNestedObject(error, ['response', 'data', 'reason']) ===
          'Unauthorized' &&
        getNestedObject(error, ['response', 'data', 'message']) ===
          'Access Denied'
      ) {
        window.location.href = sanitizeUrl(process.env.REACT_APP_LOGOUT_URL);
      }
      if (error.response) {
        return error.response;
      }
      return error;
    });
};

export default httpRequest;
