# Souls Easter Egg Hunt

Generates a series of items from specified groupings for FromSoft titles.

## Running

### Python

If you have python (v3+) on your machine you can install pandas with pip and run the script itself;

```shell
pip install pandas
```

Make sure to run the script from the project root.

```shell
python easter_egg_hunt.py
```

### Docker

Alternatively, use docker to run the script. The `scripts` directory has helper scripts to make this easier.

**Windows**

Use powershell to run the launch script. You can pass two parameters as switches;
- *build* > this will rebuild the image even if it already exists in your local registry
- *save* > this will copy the results of your easter egg hunt to your local machine. You'll find them in `./Results` at the project root.

```powershell
.\scripts\launch.ps1 -build -save
```

**Bash**

Use bash to run launch script. You can pass two flags;
- *build* > this will rebuild the image even if it already exists in your local registry
- *save* > this will copy the results of your easter egg hunt to your local machine. You'll find them in `./Results` at the project root.

```bash
./scripts/launch.sh --build --save
```