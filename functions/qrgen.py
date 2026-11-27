from InquirerPy import inquirer
from rich.console import Console
from rich.panel import Panel
import qrcode
console = Console()

def qrcodegen():
    console.print(
        Panel(
            "[bold yellow]QR Code Generator v1.0.0[/bold yellow]",
            subtitle="Sandalphon",
            border_style="green"
        )
    )
    while True:
        menu = inquirer.text(
            message="Insert a URL for your QR:"
        ).execute()
        if menu == "exit":
            return
        if menu == "":
            console.print(f"[bold red]You must insert something [/bold red]")
        img = qrcode.make(menu)
        ask = inquirer.text(
            message="Name of the file/ONLYPNG:"
        ).execute()
        if ask == "":
            console.print(f"[bold red]You must insert something [/bold red]")
            continue
        img.save(f"{ask}.png")
        console.print(f"[bold green]Saved![/bold green]")