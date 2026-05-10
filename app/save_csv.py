def save_tables_as_csv(tables):

    for i, table in enumerate(tables):

        output_file = f"output/table_{i+1}.csv"

        table.to_csv(output_file, index=False)

        print(f"Saved: {output_file}")