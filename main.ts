// Make.fun entry: news-image-20261120 - Thursday, 20 November 2026
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const src = join(__dirname, "entry.png");
const dest = "/output/entry.png";

mkdirSync(dirname(dest), { recursive: true });
copyFileSync(src, dest);
console.log(`Successfully copied ${src} to ${dest}`);
