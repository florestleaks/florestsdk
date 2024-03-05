"""    import logging
if __name__ == '__main__':

    florest_config = ForestConfiguration()
    # Configurar o LogManager com o DSN do Sentry, se aplicável
    log_manager = LogManager(log_level=logging.INFO, sentry_dsn=florest_config.internal_sentry.dsn)

    # Tags de exemplo que você deseja registrar com o log
    tags = {"feature": "processamento", "version": "1.0"}

    try:
        1/0
    except ZeroDivisionError as e:
        log_manager.log("error", message='11212', exc_info=e, category=Category.CRAWLER, task_state=TaskState.RUNNING,
                        tags=tags)
"""
