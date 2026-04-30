import argparse
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table
from matcher import match
from history import save_match, load_history, get_by_id
from fetcher import fetch_url

load_dotenv()
console = Console()

def cmd_match(args):
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            jd = f.read()
    elif args.input and args.input.startswith("http"):
        console.print("[dim]Fetching job listing...[/dim]")
        jd = fetch_url(args.input)
    elif args.input:
        jd = args.input
    else:
        console.print("[red]Provide a job description via text, URL, or -f file.txt[/red]")
        return

    console.print("[dim]Analyzing match...[/dim]")
    result = match(jd)
    save_match(result)

    console.print(f"\n[bold]{result['role']} at {result['company']}[/bold]")
    console.print(f"Fit Score: [green]{result['fit_score']}/100[/green]\n")

    console.print("[bold]Matched Skills:[/bold]")
    for s in result["matched_skills"]:
        console.print(f"  ✓ {s}")

    console.print("\n[bold]Missing Skills:[/bold]")
    for s in result["missing_skills"]:
        console.print(f"  ✗ {s}")

    console.print("\n[bold]Talking Points:[/bold]")
    for t in result["talking_points"]:
        console.print(f"  → {t}")

    console.print(f"\n[italic]{result['summary']}[/italic]")

def cmd_history(args):
    history = load_history()
    if not history:
        console.print("No matches yet.")
        return
    table = Table("ID", "Date", "Role", "Company", "Fit Score")
    for entry in history:
        table.add_row(
            str(entry["id"]),
            entry["date"],
            entry["role"],
            entry["company"],
            str(entry["fit_score"])
        )
    console.print(table)

def cmd_view(args):
    entry = get_by_id(args.id)
    if not entry:
        console.print(f"No match found with ID {args.id}")
        return
    result = entry["full_result"]
    console.print(f"\n[bold]{result['role']} at {result['company']}[/bold]")
    console.print(f"Fit Score: [green]{result['fit_score']}/100[/green]\n")
    for t in result["talking_points"]:
        console.print(f"  → {t}")
    console.print(f"\n[italic]{result['summary']}[/italic]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="job-match")
    subparsers = parser.add_subparsers()

    p_match = subparsers.add_parser("match")
    p_match.add_argument("input", nargs="?", help="Job description text or URL")
    p_match.add_argument("-f", "--file", help="Path to a .txt file containing the job description")
    p_match.set_defaults(func=cmd_match)

    p_history = subparsers.add_parser("history")
    p_history.set_defaults(func=cmd_history)

    p_view = subparsers.add_parser("view")
    p_view.add_argument("id", type=int)
    p_view.set_defaults(func=cmd_view)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()