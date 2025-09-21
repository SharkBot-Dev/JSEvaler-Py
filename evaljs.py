import asyncio

async def eval_js(code: str) -> str:
    process = await asyncio.create_subprocess_exec(
        "node", "-e", code,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate()

    output = stdout.decode().strip()
    error = stderr.decode().strip()

    return output if output else error

if __name__ == '__main__':
    async def main():
        output = await eval_js("""
console.log('HelloJSEval!')
""")
        print(output)

    asyncio.run(main())