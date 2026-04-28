import { copyFileSync, existsSync, mkdirSync, rmSync } from "node:fs";
import { join } from "node:path";

const root = process.cwd();
const outDir = join(root, "www");
const files = [
  "index.html",
  "manifest.json",
  "sw.js",
  "icon.svg",
  "local-key.js"
];

rmSync(outDir, { recursive: true, force: true });
mkdirSync(outDir, { recursive: true });

for (const file of files) {
  const source = join(root, file);
  if (!existsSync(source)) {
    throw new Error(`Missing required web asset: ${file}`);
  }
  copyFileSync(source, join(outDir, file));
}

console.log(`Prepared ${files.length} web assets in ${outDir}`);
