def init(id, cfg):
  log_info("pythonmod: init called, module id is %d port: %d script: %s" % (id, cfg.port, cfg.python_script))
  return True

def deinit(id):
  log_info("pythonmod: deinit called, module id is %d" % id)
  return True

def inform_super(id, qstate, superqstate, qdata):
  return True

def operate(id, event, qstate, qdata):
  log_info("pythonmod: operate called, id: %d, event:%s" % (id, strmodulevent(event)))

  if (event == MODULE_EVENT_NEW) or (event == MODULE_EVENT_PASS):
    if (qstate.qinfo.qtype == RR_TYPE_AAAA):
      # Create instance of DNS message (packet) with given parameters
      msg = DNSMessage(qstate.qinfo.qname_str, RR_TYPE_A, RR_CLASS_IN, PKT_QR | PKT_RA | PKT_AA)
      if not msg.set_return_msg(qstate):
        qstate.ext_state[id] = MODULE_ERROR
        return True
      # We don't need validation, result is valid
      qstate.return_msg.rep.security = 2
      qstate.return_rcode = RCODE_NOERROR
      qstate.ext_state[id] = MODULE_FINISHED
      log_info("pythonmod: blocking AAAA request for %s" % qstate.qinfo.qname_str)
      return True
    else:
      # Pass the query to validator
      qstate.ext_state[id] = MODULE_WAIT_MODULE
      return True

  if (event == MODULE_EVENT_MODDONE):
    log_info("pythonmod: module we are waiting for is done")
    qstate.ext_state[id] = MODULE_FINISHED
    return True

  log_err("pythonmod: BAD event")
  qstate.ext_state[id] = MODULE_ERROR
  return True

log_info("pythonmod: script loaded.")
