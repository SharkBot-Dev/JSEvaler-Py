# JSEvaler-Py
JavascriptをPythonから実行するためのライブラリ

# 使い方
evaljs.pyをインポートして使用してください。

# サンプルコード
```
from evaljs import eval_js
import asyncio

async def main():
    output = await eval_js("""
console.log('HelloJSEval!')
""")
    print(output)

asyncio.run(main())
```
NodeJSがインストールされている状態で実行すれば、<br>
「HelloJSEval!」と表示されるはずです。