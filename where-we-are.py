function colorText(text, colorCode) {
return `\x1b[${colorCode}m${text}\x1b[0m`;
}
function animateText(text, delay = 0.03, colorCode = "37") {
return new Promise((resolve) => {
let i = 0;
const intervalId = setInterval(() => {
process.stdout.write(colorText(text[i], colorCode));
i++;
if (i >= text.length) {
clearInterval(intervalId);
resolve();
}
}, delay * 1000);
});
}
async function singLyric(lyric, delay, colorCode) {
await new Promise((resolve) => setTimeout(resolve, delay * 1000));
await animateText(lyric, 0.03, colorCode);
console.log();
}
async function singSong() {
const lyrics = [
["\nDid we ever know?", "36"],
["Did we ever know?", "35"],
["Did we ever know?", "34"],
["\nIs it all inside of my head?", "33"],
["Maybe you still think I don't care", "31"],
["But all I need is you", "32"],
["Yeah, you know it's true", "37"],
["yeah, you know it's true", "37"],
["\nForget about where we are and let go", "36"],
["We're so close\n", "90"]
];
const delays = [0.3, 2.5, 4.4, 8.1, 12.3, 16.3, 18.7, 20.7, 23.1, 27.2];
for (let i = 0; i < lyrics.length; i++) {
const [line, colorCode] = lyrics[i];
await singLyric(line, delays[i], colorCode);
}
}
singSong();
