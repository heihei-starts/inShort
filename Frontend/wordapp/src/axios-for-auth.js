import axios from 'axios';

const instance = axios.create({
  baseURL: 'https://identitytoolkit.googleapis.com/v1' //firebaseのため変更が必要

});

export default instance;
