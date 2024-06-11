import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/components/Login.vue'
import RegisterUser from '@/components/RegisterUser.vue'
import dashboardView from '@/components/dashboard.vue'
import Productosview from '@/components/Productos.vue'
import Detalle_productoView from '@/components/Detalle_Producto.vue'
// import PromocionesView from '@/components/Promociones.vue'
// import Detalle_PromocionesView from '@/components/Detalle_promociones.vue'
// import PedidosView from '@/components/Pedidos.vue'
// import Detalle_pedidosView from '@/components/detalle_pedido.vue'
// import TransaccionView from '@/components/transaccion.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'Register',
      component: RegisterUser
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: dashboardView,
      children:[
        {path:'/personas', name: 'personas',component: RegisterUser},
        {path:'/productos', name: 'productos',component: Productosview},
        {path:'/detalle_producto', name: 'productos',component: Detalle_productoView},

       

        
      ]
    }

    
  ]
})

export default router
