import { defineConfig } from "eslint/config";
import redosPlugin from "eslint-plugin-redos";

export default defineConfig([redosPlugin.configs.flat.recommended]);
