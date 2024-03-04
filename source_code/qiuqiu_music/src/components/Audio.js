import store from '../store'
export const audioElement = new Audio();
export function playAudio() {
  audioElement.play();
}
export function adjustVolume(v) {
  store.state.nowVolume = v;
  audioElement.volume = v / 100;
}
export function pauseAudio() {
  audioElement.pause();
}

export function setTimeAudio(v) {
  audioElement.currentTime = v;
}
