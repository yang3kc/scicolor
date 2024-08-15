import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './main.css'

import { library } from '@fortawesome/fontawesome-svg-core'
/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
/* import specific icons */
import { faCopy as faCopyRegular, faCircleXmark as faCircleXmarkRegular, faTrashCan as faTrashCanRegular, faCircleLeft as faCircleLeftRegular, faCircleRight as faCircleRightRegular, faSquarePlus as faSquarePlusRegular, faCircleQuestion as faCircleQuestionRegular} from '@fortawesome/free-regular-svg-icons'
import { faGithub, faTwitter } from '@fortawesome/free-brands-svg-icons'
/* add icons to the library */
library.add(faCopyRegular, faCircleXmarkRegular, faGithub, faTrashCanRegular, faCircleLeftRegular, faCircleRightRegular, faSquarePlusRegular, faCircleQuestionRegular, faTwitter)

createApp(App).use(router).component('font-awesome-icon', FontAwesomeIcon).mount('#app')
