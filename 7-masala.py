import asyncio

async def download_data():
    print("Downloading data...")
    await asyncio.sleep(2) 
    print("Data downloaded.")

async def sending_email():
    print("Sending email...")
    await asyncio.sleep(1) 
    print("Email sent.")

async def process_data():
    print("Processing data...")
    await asyncio.sleep(3)  
    print("Data processed.")

async def main():
    await asyncio.gather(
        download_data(),
        sending_email(),
        process_data()
    )

if __name__ == "__main__":
    asyncio.run(main())
