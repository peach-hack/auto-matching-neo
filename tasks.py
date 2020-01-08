import invoke
from invoke import task


def get_file_name_tokyo(scrapy_name):
    return scrapy_name + "_tokyo.csv"


def get_file_name_kanagawa(scrapy_name):
    return scrapy_name + "_kanagawa.csv"


def get_file_name(scrapy_name):
    return scrapy_name + ".csv"


def get_file_path(file_name):
    RAWDATA_DIR = "./rawdata/"
    return RAWDATA_DIR + file_name


def create_crawl_command(area, days, scrapy_name, file_name):
    return "scrapy crawl -a area={} -a days={} {} -o {}".format(
        area, days, scrapy_name, file_name)


def crawl_base(days, name):
    rawdata_kanagawa = get_file_path(get_file_name_kanagawa(name))
    rawdata_tokyo = get_file_path(get_file_name_tokyo(name))

    try:
        invoke.run('rm {}'.format(rawdata_kanagawa))
        invoke.run('rm {}'.format(rawdata_tokyo))
    except Exception:
        pass
    invoke.run(create_crawl_command("神奈川県", days, name, rawdata_kanagawa))
    invoke.run(create_crawl_command("東京都", days, name, rawdata_tokyo))


def crawl_base_kanagawa(days, name):
    rawdata_kanagawa = get_file_path(get_file_name_kanagawa(name))

    try:
        invoke.run('rm {}'.format(rawdata_kanagawa))
    except Exception:
        pass
    invoke.run(create_crawl_command("神奈川県", days, name, rawdata_kanagawa))


def crawl_base_tokyo(days, name):
    rawdata_tokyo = get_file_path(get_file_name_tokyo(name))

    try:
        invoke.run('rm {}'.format(rawdata_tokyo))
    except Exception:
        pass
    invoke.run(create_crawl_command("東京都", days, name, rawdata_tokyo))


@task
def crawl_wakuwaku(c, days):
    name = "wakuwaku"
    crawl_base(days, name)


@task
def crawl_wakuwaku_tokyo(c, days):
    name = "wakuwaku"
    crawl_base_tokyo(days, name)


@task
def crawl_wakuwaku_kanagawa(c, days):
    name = "wakuwaku"
    crawl_base_kanagawa(days, name)


@task
def crawl_happymail(c):
    name = "happymail"
    crawl_base(1, name)


@task
def crawl_happymail_tokyo(c):
    name = "happymail"
    crawl_base_tokyo(1, name)


@task
def crawl_happymail_kanagawa(c):
    name = "happymail"
    crawl_base_kanagawa(1, name)


@task
def crawl_pcmax(c):
    name = "pcmax"
    crawl_base(1, name)


@task
def crawl_pcmax_tokyo(c):
    name = "pcmax"
    crawl_base_tokyo(1, name)


@task
def crawl_pcmax_kanagawa(c):
    name = "pcmax"
    crawl_base_kanagawa(1, name)


@task
def crawl_ikukuru(c, days):
    name = "ikukuru"
    crawl_base(days, name)


@task
def crawl_ikukuru_tokyo(c, days):
    name = "ikukuru"
    crawl_base_tokyo(days, name)


@task
def crawl_ikukuru_kanagawa(c, days):
    name = "ikukuru"
    crawl_base_kanagawa(days, name)


@task
def crawl_mint(c):
    name = "mint"
    crawl_base(1, name)


@task
def crawl_mint_tokyo(c):
    name = "mint"
    crawl_base_tokyo(1, name)


@task
def crawl_mint_kanagawa(c):
    name = "mint"
    crawl_base_kanagawa(1, name)


@task
def crawl_merupara(c):
    name = "merupara"
    crawl_base(1, name)


@task
def crawl_merupara_tokyo(c):
    name = "merupara"
    crawl_base_tokyo(1, name)


@task
def crawl_merupara_kanagawa(c):
    name = "merupara"
    crawl_base_kanagawa(1, name)


@task
def crawl_from_cron(c):
    crawl_happymail(c)
    crawl_wakuwaku(c, 1)
    crawl_pcmax(c)
    crawl_ikukuru(c, 1)
    crawl_mint(c)
    crawl_merupara(c)


def create_search_command(keyword, scrapy_name, file_name):
    return "scrapy crawl -a keyword={} {} -o {}".format(
        keyword, scrapy_name, file_name)


def search_base(keyword, name):
    rawdata = get_file_path(get_file_name(name))

    try:
        invoke.run('rm {}'.format(rawdata))
    except Exception:
        pass
    invoke.run(create_search_command(keyword, name, rawdata))


@task
def search_wakuwaku(c, keyword):
    name = "wakuwaku_search"
    search_base(keyword, name)
