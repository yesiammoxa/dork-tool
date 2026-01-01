#!/usr/bin/env python3
# Multi Search Dorking Tool - by moxa

import urllib.parse
import os
import webbrowser

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

SEARCH_ENGINES = {
    "1": ("Google", "https://www.google.com/search?q="),
    "2": ("Bing", "https://www.bing.com/search?q="),
    "3": ("DuckDuckGo", "https://duckduckgo.com/?q="),
    "4": ("Yandex", "https://yandex.com/search/?text=")
}

def banner():
    os.system("clear" if os.name == "posix" else "cls")
    print(RED + """
 ██████╗  ██████╗ ██████╗ ██╗  ██╗
 ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝
 ██║  ██║██║   ██║██████╔╝█████╔╝ 
 ██║  ██║██║   ██║██╔══██╗██╔═██╗ 
 ██████╔╝╚██████╔╝██║  ██║██║  ██╗
 ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
              v1.0
""" + RESET)

def build_filetype_dork(filetypes):
    types = [f"filetype:{ft.strip()}" for ft in filetypes.split(",") if ft.strip()]
    if len(types) > 1:
        return "(" + " OR ".join(types) + ")"
    return types[0] if types else None

def build_dork(keyword, filetypes=None, site=None, extra=None):
    if " " in keyword:
        keyword = f'"{keyword}"'

    parts = [keyword]

    if filetypes:
        parts.append(build_filetype_dork(filetypes))

    if site:
        parts.append(f"site:{site}")

    if extra:
        parts.append(extra)

    return " ".join(filter(None, parts))

def main():
    banner()

    print(GREEN + "[+] Select search engine:" + RESET)
    for k, v in SEARCH_ENGINES.items():
        print(f"  {k}) {v[0]}")

    engine_choice = input("\n[+] Engine number: ").strip()
    engine = SEARCH_ENGINES.get(engine_choice)

    if not engine:
        print(RED + "[-] Invalid choice" + RESET)
        return

    keyword = input("[+] Keyword: ").strip()
    filetypes = input("[+] File types (pdf,sql,env) [optional]: ").strip()
    site = input("[+] Domain or TLD [optional]: ").strip()
    extra = input("[+] Extra dork (inurl, intitle..) [optional]: ").strip()

    dork = build_dork(
        keyword,
        filetypes if filetypes else None,
        site if site else None,
        extra if extra else None
    )

    query = urllib.parse.quote(dork)
    search_url = engine[1] + query

    print("\n" + GREEN + "[✓] Generated dork:" + RESET)
    print(dork)

    print("\n" + BLUE + "[✓] Search URL:" + RESET)
    print(search_url)

    open_now = input("\n[?] Open link in browser? (y/n): ").lower()
    if open_now == "y":
        webbrowser.open(search_url)

if __name__ == "__main__":
    main()
