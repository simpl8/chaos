<template>
    <div class='login'>
        <h1> {{ titleMsg }}</h1>
        <el-form ref="loginForm" :model="loginData" label-width="100px" >
            <el-form-item label="用户名" prop="username" :rules="[{required: true, message: '用户名不能为空'}]"><br>
                <el-input style="width: 400px" ref="username" type="password" v-model="loginData.username" autocomplete="off"></el-input>
            </el-form-item>
        <el-form-item label="密码" prop="password" :rules="[{required: true, message: '密码不能为空'}]"><br>
            <el-input style="width: 400px" type="password" v-model="loginData.password" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item>
            <el-button type="parimary" @click="loginForm('loginForm')">登录</el-button>
            <el-button @click="resetForm('loginForm')">注册</el-button>
        </el-form-item>
        </el-form>
    </div>    
</template>

<script>
import qs from 'qs'
import service from '../utils/request'
import Cookies from 'js-cookie'

export default {
    name: 'loginForm',
    data() {
        return {
            titleMsg: '欢迎使用chaos平台',
            loginData: {
                username: '',
                password: ''
            }
        }
    },
    methods: {
        loginForm(formName) {
          this.$refs[formName].validate((valid) => {
           if (valid) {
             service({url: '/login', method: 'post', data: qs.stringify(this.loginData)})
             .then(response => {
               const { data } = response
               Cookies.set('Authorization', data.data.token)
               alert("submit!!!" + '\n' + data.msg)
             })
             .catch(error => {
               console.log(error)
             })
           } else {
            console.log('illegad submit!!');
            return false;
          }
        })
      },
        resetForm(formName) {
                this.$refs[formName].resetFields()
                console.log('reset')
        },
    }

}

</script>