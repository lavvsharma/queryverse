from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['settings.toml', '.secrets.toml'],
)

log_file_name = settings["logger"]["file_name"]
log_file_max_size = settings["logger"]["file_max_size"]
log_create_new_log_at = settings["logger"]["create_new_log_at"]
log_clean_log_after = settings["logger"]["clean_log_after"]
