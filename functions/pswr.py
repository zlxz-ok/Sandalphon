import secrets
from InquirerPy import inquirer
import string
from rich.console import Console
from rich.panel import Panel
import pyperclip
console = Console()

def password():
    console.print(
        Panel(
            "[bold yellow]Password Generator v1.0.0[/bold yellow]",
            subtitle="Sandalphon",
            border_style="purple"
        )
    )
    while True:
        strings = ""
        passw = ""
        menu = inquirer.checkbox(
            message="Select an option for your password:",
            choices=[
                "Lower case",
                "Upper case",
                "Numbers",
                "Symbols",
                "Exit"
            ],
            pointer="❯",
            enabled_symbol="[✓]",
            disabled_symbol="[ ]"   
        ).execute()
        if "Exit" in menu:
            return
        if not menu:
          console.print("[bold red]You must select at least one option![/bold red]")
          continue
        if "Lower case" in menu:
            strings += string.ascii_lowercase
        if "Upper case" in menu:
            strings += string.ascii_uppercase
        if "Numbers" in menu:
            strings += string.digits
        if "Symbols" in menu:
            strings += string.punctuation
        ask = inquirer.number(
            message="How many digits?",
            float_allowed=False
        ).execute()
        if int(ask) <= 0:
           console.print("[bold red]Fail,Please Try Again![/bold red]")
           continue
        if int(ask) >= 1000:
           console.print("[bold red]Fail,Too many numbers[/bold red]")
           continue
        for x in range(int(ask)):
            passw = passw + secrets.choice(strings)
        console.print(f"[bold red]Your password is:[/bold red]{passw}")
        tryar = True
        while tryar:
         trya = inquirer.select(
             message="Select an option:",
             choices=[
                 "Regenerate",
                 "Copy to clipboard",
                 "Exit"
             ]
         ).execute()
         if trya == "Regenerate":
           #Confirm regenerate
           confrg = inquirer.confirm(
              message="Regenerate?"
           ).execute()
           if confrg:
            passw = ""
            for x in range(int(ask)):
                passw = passw + secrets.choice(strings)
            console.print(f"[bold red]Your password is:[/bold red]{passw}")
           else:
              continue
         elif trya == "Copy to clipboard":
            try:
             pyperclip.copy(passw)
            except Exception as e:
               console.print(f"[bold red]Failed!,errror:{e}[/bold red]")
            console.print("[bold green]Password copied to clipboard![/bold green]")
         elif trya == "Exit":
            console.clear()
            tryar = False
            console.print(
                 Panel(
                    "[bold yellow]Password Generator v1.0.0[/bold yellow]",
                    subtitle="Sandalphon",
                    border_style="black"
                    )
                 )
            