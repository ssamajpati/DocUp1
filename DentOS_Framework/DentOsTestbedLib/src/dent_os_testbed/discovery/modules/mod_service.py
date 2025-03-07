# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/dent/system/os/service.yaml
#
# DONOT EDIT - generated by diligent bots

from dent_os_testbed.discovery.Module import Module
from dent_os_testbed.lib.os.service import Service


class ServiceMod(Module):
    """ """

    def set_service(self, src, dst):

        for i, service in enumerate(src):
            if "name" in service:
                dst[i].name = service.get("name")
            if "loaded" in service:
                dst[i].loaded = service.get("loaded")
            if "active" in service:
                dst[i].active = service.get("active")
            if "status" in service:
                dst[i].status = service.get("status")
            if "description" in service:
                dst[i].description = service.get("description")

    async def discover(self):
        # need to get device instance to get the data from
        #
        for i, dut in enumerate(self.report.duts):
            if not dut.device_id:
                continue
            dev = self.ctx.devices_dict[dut.device_id]
            if dev.os == "ixnetwork" or not await dev.is_connected():
                print("Device not connected skipping service discovery")
                continue
            print("Running service Discovery on " + dev.host_name)
            out = await Service.show(
                input_data=[{dev.host_name: [{"dut_discovery": True}]}],
                device_obj={dev.host_name: dev},
                parse_output=True,
            )
            if out[0][dev.host_name]["rc"] != 0:
                print(out)
                print("Failed to get service")
                continue
            if "parsed_output" not in out[0][dev.host_name]:
                print("Failed to get parsed_output service")
                print(out)
                continue
            self.set_service(
                out[0][dev.host_name]["parsed_output"], self.report.duts[i].system.os.services
            )
            print(
                "Finished service Discovery on {} with {} entries".format(
                    dev.host_name, len(self.report.duts[i].system.os.services)
                )
            )
