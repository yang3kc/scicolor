<script setup>
import { ref } from 'vue';

// data
const ToastShown = ref(false);
const ToastMessage = ref('');
const ToastMessageColor = ref('');

// methods
const showToast = (message, color) => {
    console.log(message, color);
    ToastShown.value = true;
    ToastMessage.value = message;
    ToastMessageColor.value = color;
    setTimeout(() => {
        ToastShown.value = false;
    }, 3000);
}

const getTextColor = (backgroundColor) => {
    let lightColor = 'white';
    let darkColor = 'black';
    let color = (backgroundColor.charAt(0) === '#') ? backgroundColor.substring(1, 7) : backgroundColor;
    let r = parseInt(color.substring(0, 2), 16); // hexToR
    let g = parseInt(color.substring(2, 4), 16); // hexToG
    let b = parseInt(color.substring(4, 6), 16); // hexToB
    return (((r * 0.299) + (g * 0.587) + (b * 0.114)) > 186) ? darkColor : lightColor;
}

defineExpose({
    showToast
});
</script>

<template>
    <div v-if="ToastShown" class="toast" :style="{ backgroundColor: ToastMessageColor, color: getTextColor(ToastMessageColor) }">
        {{ ToastMessage }}
    </div>
</template>