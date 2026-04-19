from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

ALLOWED_IPS = ["10.0.0.1", "10.0.0.2"]

def _handle_PacketIn(event):
    packet = event.parsed

    # Allow ARP
    if packet.type == 0x0806:
        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        event.connection.send(msg)
        return

    ip = packet.find('ipv4')
    if not ip:
        return

    src = str(ip.srcip)
    dst = str(ip.dstip)

    log.info(f"{src} -> {dst}")

    if src not in ALLOWED_IPS:
        log.info(f"BLOCKED: {src}")
        return

    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Access Control Running")