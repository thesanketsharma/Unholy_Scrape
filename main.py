import pandas as pd

# Save onion_check results to Excel
def save_onion_check_results(results, filename="results.xlsx"):
    df = pd.DataFrame(results)
    with pd.ExcelWriter(filename, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
        df.to_excel(writer, sheet_name="Onion_Check", index=False)

# Save recon results
def save_recon_results(recon_outputs, filename="results.xlsx"):
    data = []
    for r in recon_outputs:
        data.append({"Header": r["header"], "Output": "\n".join(r["output"])})
    df = pd.DataFrame(data)
    with pd.ExcelWriter(filename, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
        df.to_excel(writer, sheet_name="Recon", index=False)

# Save headers results
def save_headers_results(domains, filename="results.xlsx"):
    data = []
    for d in domains:
        data.append({
            "URL": d["title"],
            "Headers": json.dumps(dict(d["headers"])),  # store headers as JSON string
            "Screenshot": d.get("screenshot", "N/A")
        })
    df = pd.DataFrame(data)
    with pd.ExcelWriter(filename, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
        df.to_excel(writer, sheet_name="Headers", index=False)

# Save enumeration results
def save_enumeration_results(enumeration_outputs, filename="results.xlsx"):
    data = []
    for e in enumeration_outputs:
        data.append({
            "Onion_Link": e["onion_link"],
            "Feroxbuster_Output": e["feroxbuster_output"]
        })
    df = pd.DataFrame(data)
    with pd.ExcelWriter(filename, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
        df.to_excel(writer, sheet_name="Enumeration", index=False)
