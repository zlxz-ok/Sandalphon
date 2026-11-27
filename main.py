from functions.metafile import metafile
from functions.pswr import password
from functions.qrgen import qrcodegen
from InquirerPy import inquirer
from rich.console import Console
from rich.panel import Panel
console = Console()
def main():
    while True:
        console.print(
            Panel(
                "[bold purple]Sandalphon v1.0.0[/bold purple]",
                title="",
                border_style="blue"
            )
        )
        menu = inquirer.select(
            message="Select an option:",
            choices=[
                "Metadata Inspector",
                "Password Generator",
                "QR Code Generator",
                "Exit",
            ]
        ).execute()
        if menu == "Metadata Inspector":
            console.clear()
            metafile()
        elif menu == "Password Generator":
            console.clear()
            password()
        elif menu == "QR Code Generator":
            console.clear()
            qrcodegen()
        elif menu == "Exit":
            return
if __name__ == "__main__":
    main()