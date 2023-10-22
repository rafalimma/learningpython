from log import LogFileMixin, LogPrintMixin

lp = LogPrintMixin()
lp.log_error('qualquer coisa')
lp.log_sucess('q legal')
lf = LogFileMixin()
lf.log_error('qualquer coisa')
lf.log_sucess('q legal')