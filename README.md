# Challenge Yungas

This is a [Yungas](https://www.yungas.com.br/) challenge API project.

Follow the steps below to run the project locally

## Get started

*Note that you will need to have [Phyton](https://www.python.org/), [pip](https://pypi.org/project/pip/) and [virtualenv](https://pypi.org/project/pip/) installed.*

Clone the project...

```bash
git clone https://github.com/IgorVessali/challenge-yungas-api.git 
cd challenge-yungas
```

Create and activate the virtualenv...

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies...

```bash
pip install -r requirements.txt
```

Now start the project:

```bash
python app.py
```

Navigate to [localhost:5000](http://127.0.0.1:5000/) and see the project running.

Run the tests...

```bash
pytest  
```