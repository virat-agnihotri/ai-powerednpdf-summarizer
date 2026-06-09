import os 
from tkinter import Tk, filedialog
from supabase import create_client, Client

# 1. Initialize Supabase Client
# Replace these with your actual Supabase Project URL and Anon API key
SUPABASE_URL: str = "https://qzvwnjpugmbjzwvhcjtr.supabase.co"
SUPABASE_KEY: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InF6dnduanB1Z21ianp3dmhjanRyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODA5MzAxNjYsImV4cCI6MjA5NjUwNjE2Nn0.oZBiAm2QjMmTRnfxa5lMDlUGRtonbp5T0hvesbrapLQ" 
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Define the exact bucket name you created in your Supabase dashboard
BUCKET_NAME = "pdfs" 

def open_file_explorer():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    selected_file_path = filedialog.askopenfilename(
        title="Select your PDF to upload to the cloud",
        filetypes=[("PDF files", "*.pdf")]
    )
    if selected_file_path:
        print(f"Success! You selected: {selected_file_path}")
        print(f"File Name: {os.path.basename(selected_file_path)}")
        return selected_file_path
    else:
        print("User cancelled or closed the file explorer.")
        return None

def upload_to_supabase(file_path):
    """
    Takes a local file path, reads the file in binary mode, 
    and uploads it directly to the Supabase storage bucket.
    """
    if not file_path:
        return None

    # Extract just the filename (e.g., "document.pdf") to use as the storage path
    file_name = os.path.basename(file_path)

    try:
        # Open the file in binary read mode ('rb')
        with open(file_path, "rb") as file_data:
            print(f"Uploading '{file_name}' to Supabase storage bucket '{BUCKET_NAME}'...")
            
            # Execute the upload
            response = supabase.storage.from_(BUCKET_NAME).upload(
                file=file_data,
                path=file_name, # Storing it at the root of the bucket with its original filename
                file_options={
                    "content-type": "application/pdf",
                    "upsert": "true" # Overwrites the file seamlessly if it already exists
                }
            )
        
        print("✓ Upload successful!")
        # Return the file name so pdf_processor.py knows exactly what file to pull down next
        return file_name

    except Exception as e:
        print(f"✗ Upload failed: {e}")
        return None

# --- Main Execution Flow ---
if __name__ == "__main__":
    # Step 1: Open file explorer and get path
    pdf_to_upload = open_file_explorer()
    
    # Step 2: Pass that path directly to the Supabase upload function
    if pdf_to_upload:
        uploaded_filename = upload_to_supabase(pdf_to_upload)
        if uploaded_filename:
            print(f"Ready for processing. Saved identifier: {uploaded_filename}")