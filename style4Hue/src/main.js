import './app.css'
//import App from './App.svelte'
import Home from './Home.svelte'


/*
const app = new App({
  target: document.getElementById('app'),
})
*/

const home = new Home({
  target: document.getElementById('home'),
})

//export default app
export default home
