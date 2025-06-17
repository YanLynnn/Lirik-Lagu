function animateText(text, delay = 50) {
return new Promise((resolve) => {
let i = 0;
const interval = setInterval(() => {
process.stdout.write(text[i]);
i++;
if (i >= text.length) {
clearInterval(interval);
process.stdout.write('\n');
resolve();
}
}, delay);
});
}
async function singLyric(lyric, delay, speed, lineDelay = 0) {
await new Promise((r) => setTimeout(r, delay * 1000));
await animateText(lyric, speed * 1000);
await new Promise((r) => setTimeout(r, lineDelay * 1000));
}
async function singSong() {
const lyrics = [
["Tante...", 0.08],
["Sudah terbiasa terjadi tante...", 0.09],
["Teman datang cuma kalo butuh saja...", 0.08],
["Coba kalau lagi susah...", 0.15],
["Mereka semua menghilaaaaang...", 0.15],
];
const delays = [0.3, 2.5, 5.8, 9.5, 13.5];
const tasks = lyrics.map(([lyric, speed], i) =>
singLyric(lyric, delays[i], speed)
);
await Promise.all(tasks);
}
singSong();
