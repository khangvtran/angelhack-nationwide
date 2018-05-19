import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/pages/HelloWorld'
import start_button from '@/components/start_button'
import zillowpage from '@/pages/zillowpage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
    	path:'/test',
    	name: 'start_button',
    	component: start_button
    },
    {
    	path:'/placeholder',
    	name: 'zillowpage',
    	component: zillowpage
    }
  ]
})
