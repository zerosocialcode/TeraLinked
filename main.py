import sys
import os
import time
from contextlib import contextmanager
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from TeraboxDL import TeraboxDL

console = Console()

# 🔐 Your saved cookie (replace with your actual values from Step 2 above)
COOKIE = "lang=en; ndus=YS4sigYteHuiw7UWLc_O1bLkLaVksR5S7O9iRrqM;"

# 🔇 Suppress stdout (to hide TeraboxDL banner)
@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

def main():
    console.print(Panel("📦 [bold cyan]TeraBox Direct Download Link Generator[/bold cyan]", expand=False))

    # Initialize downloader without printing banner
    with suppress_stdout():
        terabox = TeraboxDL(COOKIE)

    while True:
        link = Prompt.ask("\n[green]Enter TeraBox shared link[/green] (or type 'exit' to quit)")
        if link.lower() == "exit":
            console.print("\n[bold red]👋 Exiting...[/bold red]")
            break

        with console.status("[bold blue]Processing...[/bold blue]", spinner="dots"):
            try:
                file_info = terabox.get_file_info(link)
                time.sleep(1)

                if "error" in file_info:
                    console.print(f"[bold red]❌ Error:[/bold red] {file_info['error']}")
                else:
                    console.print("\n[bold green]✅ File Info:[/bold green]")
                    console.print(f"[cyan]📁 File Name:[/cyan] {file_info.get('file_name', 'N/A')}")
                    console.print(f"[cyan]📦 File Size:[/cyan] {file_info.get('size', 'N/A')}")

                    download_link = file_info.get("download_link")
                    if download_link:
                        console.print(f"\n[bold magenta]🔗 Direct Download Link:[/bold magenta]\n{download_link}")
                    else:
                        console.print("[yellow]⚠️ Direct download link not found.[/yellow]")

            except Exception as e:
                console.print(f"[red]🚨 Unexpected Error:[/red] {str(e)}")

if __name__ == "__main__":
    main()
