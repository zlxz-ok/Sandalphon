from pathlib import Path
from datetime import datetime
from InquirerPy import inquirer
from rich.console import Console
from rich.panel import Panel
from PIL import Image
console = Console()
import mimetypes
def metafile():
    console.print(
        Panel(
            "[bold yellow]Metadata Inspector v1.0.0[/bold yellow]",
            subtitle="Sandalphon",
            border_style="black"
        )
    )
    try:
        while True:
            menu = inquirer.text(
                message="Insert the path of the file:"
            ).execute()
            if menu == "exit":
                console.clear()
                return
            p = Path(menu)
            p = p.expanduser()
            if p.is_file():
                metadata = p.stat()
                date = datetime.fromtimestamp(metadata.st_mtime)
                a,b = mimetypes.guess_type(p)
                if a and a.startswith("image/"):
                    try:
                        img = Image.open(p)
                        img.verify()
                        img = Image.open(p)
                    except Exception as e:
                        console.print(f"[bold red]Unable to read image: {e}[/bold red]")
                        continue
                    exif = img.getexif()
                    if not exif:
                       exif = "No EXIF"
                    else:
                      pass    
                    console.print(f"[bold black]Image Detected:[/bold black]")
                    console.print(f"[bold black]Name:[/bold black][bold yellow]{p.name}")
                    console.print(f"[bold black]Size:[/bold black][bold yellow]{metadata.st_size}")
                    console.print(f"[bold black]MIME type:[/bold black][bold yellow]{a}")
                    console.print(f"[bold black]Format:[/bold black][bold yellow]{img.format}")
                    console.print(f"[bold black]Resolution:[/bold black][bold yellow]{img.size}")
                    console.print(f"[bold black]EXIF:[/bold black][bold yellow]{exif}")
                    console.print(f"[bold black]Last Modified:[/bold black][bold yellow]{date.strftime("%d/%m/%Y %H:%M")}")
                else:
                    console.print(f"[bold black]Name:[/bold black][bold yellow]{p.name}")
                    console.print(f"[bold black]Size:[/bold black][bold yellow]{metadata.st_size}")
                    console.print(f"[bold black]MIME type:[/bold black][bold yellow]{a}")
                    console.print(f"[bold black]Last Modified:[/bold black][bold yellow]{date.strftime("%d/%m/%Y %H:%M")}")
            else:
                console.print(f"[bold red]Insert a valid path![/bold red]")
    except Exception as e:
        console.print(f"[bold red]An error occurred: {e}[/bold red]")