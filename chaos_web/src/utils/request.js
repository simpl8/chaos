import axios from 'axios'
import Cookies from 'js-cookie'

// axios.defaults.withCredentials = true
/*------创建axios实例------ */
const servie = axios.create({
  baseURL: 'http://localhost:1908', //api的base_url
  timeout: 5000, //请求超时时间
})

servie.interceptors.request.use(
  config => {
    config.headers['Authorization'] = Cookies.get("Authorization")
    return config
  },
  error => {
    console.log(error)
    return Promise.reject(error)
  }
)

export default servie