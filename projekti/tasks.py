from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/main.py")

@task 
def run_tests(ctx):
    ctx.run("pytest")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")