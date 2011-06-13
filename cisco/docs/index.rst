======================
blockdiagcontrib-cisco
======================
A plugin for `blockdiag` that provides shapes for networking.
The shapes are using `Network Topology Icons`_ designed by `Cisco Systems, Inc`_ .

.. _Network Topology Icons: http://www.cisco.com/web/about/ac50/ac47/2.html
.. _Cisco Systems, Inc: http://www.cisco.com/

Diagram examples
================
`blockdiagcontrib-cisco` renders network icon as node's shape.

Example::

   diagram admin {
     A [shape = "cisco.router"];
   }

.. blockdiag::

   diagram admin {
     A [shape = "cisco.router"];
   }

Or, use `shape_namespace` keyword::

   diagram admin {
     shape_namespace = "cisco";

     A [shape = "router"];
   }

.. blockdiag::

   diagram admin {
     shape_namespace = "cisco";

     A [shape = "router"];
   }

See more examples and output images in http://packages.python.org/blockdiagcontrib-cisco/ .


Requirements
============
* blockdiag 0.8.0 or later


License
=======
Python Software Foundation License.


Shapes
=======

.. list-table::
   :header-rows: 0

   * - shape = "cisco.printer"

       .. blockdiag::

          { A [label = '', shape = 'cisco.printer']; }

     - shape = "cisco.multilayer_remote_switch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.multilayer_remote_switch']; }

     - shape = "cisco.voice_commserver"

       .. blockdiag::

          { A [label = '', shape = 'cisco.voice_commserver']; }

   * - shape = "cisco.ons15500"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ons15500']; }

     - shape = "cisco.guard"

       .. blockdiag::

          { A [label = '', shape = 'cisco.guard']; }

     - shape = "cisco.atm_fast_gigabit_etherswitch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.atm_fast_gigabit_etherswitch']; }

   * - shape = "cisco.truck"

       .. blockdiag::

          { A [label = '', shape = 'cisco.truck']; }

     - shape = "cisco.vault"

       .. blockdiag::

          { A [label = '', shape = 'cisco.vault']; }

     - shape = "cisco.lan_to_lan"

       .. blockdiag::

          { A [label = '', shape = 'cisco.lan_to_lan']; }

   * - shape = "cisco.Space_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.Space_router']; }

     - shape = "cisco.dpt"

       .. blockdiag::

          { A [label = '', shape = 'cisco.dpt']; }

     - shape = "cisco.iscsi_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.iscsi_router']; }

   * - shape = "cisco.ip_dsl"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ip_dsl']; }

     - shape = "cisco.CUBE"

       .. blockdiag::

          { A [label = '', shape = 'cisco.CUBE']; }

     - shape = "cisco.standard_host"

       .. blockdiag::

          { A [label = '', shape = 'cisco.standard_host']; }

   * - shape = "cisco.ics"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ics']; }

     - shape = "cisco.antenna"

       .. blockdiag::

          { A [label = '', shape = 'cisco.antenna']; }

     - shape = "cisco.cloud"

       .. blockdiag::

          { A [label = '', shape = 'cisco.cloud']; }

   * - shape = "cisco.system_controller"

       .. blockdiag::

          { A [label = '', shape = 'cisco.system_controller']; }

     - shape = "cisco.sun_workstation"

       .. blockdiag::

          { A [label = '', shape = 'cisco.sun_workstation']; }

     - shape = "cisco.fibre_channel_fabric_switch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.fibre_channel_fabric_switch']; }

   * - shape = "cisco.netflow_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.netflow_router']; }

     - shape = "cisco.content_transformation_engine_(cte)"

       .. blockdiag::

          { A [label = '', shape = 'cisco.content_transformation_engine_(cte)']; }

     - shape = "cisco.route_switch_processor"

       .. blockdiag::

          { A [label = '', shape = 'cisco.route_switch_processor']; }

   * - shape = "cisco.transpath"

       .. blockdiag::

          { A [label = '', shape = 'cisco.transpath']; }

     - shape = "cisco.ssl_terminator"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ssl_terminator']; }

     - shape = "cisco.page_icon"

       .. blockdiag::

          { A [label = '', shape = 'cisco.page_icon']; }

   * - shape = "cisco.optical_services_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.optical_services_router']; }

     - shape = "cisco.relational_database"

       .. blockdiag::

          { A [label = '', shape = 'cisco.relational_database']; }

     - shape = "cisco.generic_softswitch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.generic_softswitch']; }

   * - shape = "cisco.upc"

       .. blockdiag::

          { A [label = '', shape = 'cisco.upc']; }

     - shape = "cisco.ups"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ups']; }

     - shape = "cisco.layer_2_remote_switch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.layer_2_remote_switch']; }

   * - shape = "cisco.modem"

       .. blockdiag::

          { A [label = '', shape = 'cisco.modem']; }

     - shape = "cisco.fibre_channel_disk_subsystem"

       .. blockdiag::

          { A [label = '', shape = 'cisco.fibre_channel_disk_subsystem']; }

     - shape = "cisco.vpn_concentrator"

       .. blockdiag::

          { A [label = '', shape = 'cisco.vpn_concentrator']; }

   * - shape = "cisco.software_based_server"

       .. blockdiag::

          { A [label = '', shape = 'cisco.software_based_server']; }

     - shape = "cisco.mesh_ap"

       .. blockdiag::

          { A [label = '', shape = 'cisco.mesh_ap']; }

     - shape = "cisco.virtual_layer_switch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.virtual_layer_switch']; }

   * - shape = "cisco.3x74_(floor)"

       .. blockdiag::

          { A [label = '', shape = 'cisco.3x74_(floor)']; }

     - shape = "cisco.6700_series"

       .. blockdiag::

          { A [label = '', shape = 'cisco.6700_series']; }

     - shape = "cisco.VSD"

       .. blockdiag::

          { A [label = '', shape = 'cisco.VSD']; }

   * - shape = "cisco.umg_series"

       .. blockdiag::

          { A [label = '', shape = 'cisco.umg_series']; }

     - shape = "cisco.fileserver"

       .. blockdiag::

          { A [label = '', shape = 'cisco.fileserver']; }

     - shape = "cisco.macintosh"

       .. blockdiag::

          { A [label = '', shape = 'cisco.macintosh']; }

   * - shape = "cisco.www_server"

       .. blockdiag::

          { A [label = '', shape = 'cisco.www_server']; }

     - shape = "cisco.ip"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ip']; }

     - shape = "cisco.wireless_location_appliance"

       .. blockdiag::

          { A [label = '', shape = 'cisco.wireless_location_appliance']; }

   * - shape = "cisco.ASR_1000_Series"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ASR_1000_Series']; }

     - shape = "cisco.tablet"

       .. blockdiag::

          { A [label = '', shape = 'cisco.tablet']; }

     - shape = "cisco.lock"

       .. blockdiag::

          { A [label = '', shape = 'cisco.lock']; }

   * - shape = "cisco.car"

       .. blockdiag::

          { A [label = '', shape = 'cisco.car']; }

     - shape = "cisco.scanner"

       .. blockdiag::

          { A [label = '', shape = 'cisco.scanner']; }

     - shape = "cisco.safeharbor_icon"

       .. blockdiag::

          { A [label = '', shape = 'cisco.safeharbor_icon']; }

   * - shape = "cisco.me_1100"

       .. blockdiag::

          { A [label = '', shape = 'cisco.me_1100']; }

     - shape = "cisco.localdirector"

       .. blockdiag::

          { A [label = '', shape = 'cisco.localdirector']; }

     - shape = "cisco.mau"

       .. blockdiag::

          { A [label = '', shape = 'cisco.mau']; }

   * - shape = "cisco.front_end_processor"

       .. blockdiag::

          { A [label = '', shape = 'cisco.front_end_processor']; }

     - shape = "cisco.hub"

       .. blockdiag::

          { A [label = '', shape = 'cisco.hub']; }

     - shape = "cisco.voice_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.voice_router']; }

   * - shape = "cisco.ratemux"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ratemux']; }

     - shape = "cisco.network_management"

       .. blockdiag::

          { A [label = '', shape = 'cisco.network_management']; }

     - shape = "cisco.ios_slb"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ios_slb']; }

   * - shape = "cisco.government_building"

       .. blockdiag::

          { A [label = '', shape = 'cisco.government_building']; }

     - shape = "cisco.iad_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.iad_router']; }

     - shape = "cisco.mac_woman"

       .. blockdiag::

          { A [label = '', shape = 'cisco.mac_woman']; }

   * - shape = "cisco.communications_server"

       .. blockdiag::

          { A [label = '', shape = 'cisco.communications_server']; }

     - shape = "cisco.file_server"

       .. blockdiag::

          { A [label = '', shape = 'cisco.file_server']; }

     - shape = "cisco.cs-mars"

       .. blockdiag::

          { A [label = '', shape = 'cisco.cs-mars']; }

   * - shape = "cisco.iptv_content_manager"

       .. blockdiag::

          { A [label = '', shape = 'cisco.iptv_content_manager']; }

     - shape = "cisco.dual_mode_ap"

       .. blockdiag::

          { A [label = '', shape = 'cisco.dual_mode_ap']; }

     - shape = "cisco.turret"

       .. blockdiag::

          { A [label = '', shape = 'cisco.turret']; }

   * - shape = "cisco.sitting_woman"

       .. blockdiag::

          { A [label = '', shape = 'cisco.sitting_woman']; }

     - shape = "cisco.Services"

       .. blockdiag::

          { A [label = '', shape = 'cisco.Services']; }

     - shape = "cisco.mini_vax"

       .. blockdiag::

          { A [label = '', shape = 'cisco.mini_vax']; }

   * - shape = "cisco.meetingplace"

       .. blockdiag::

          { A [label = '', shape = 'cisco.meetingplace']; }

     - shape = "cisco.octel"

       .. blockdiag::

          { A [label = '', shape = 'cisco.octel']; }

     - shape = "cisco.dwdm_filter"

       .. blockdiag::

          { A [label = '', shape = 'cisco.dwdm_filter']; }

   * - shape = "cisco.fax"

       .. blockdiag::

          { A [label = '', shape = 'cisco.fax']; }

     - shape = "cisco.pc_adapter_card"

       .. blockdiag::

          { A [label = '', shape = 'cisco.pc_adapter_card']; }

     - shape = "cisco.netsonar"

       .. blockdiag::

          { A [label = '', shape = 'cisco.netsonar']; }

   * - shape = "cisco.web_cluster"

       .. blockdiag::

          { A [label = '', shape = 'cisco.web_cluster']; }

     - shape = "cisco.gigabit_switch_atm_tag_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.gigabit_switch_atm_tag_router']; }

     - shape = "cisco.stb"

       .. blockdiag::

          { A [label = '', shape = 'cisco.stb']; }

   * - shape = "cisco.content_engine_(cache_director)"

       .. blockdiag::

          { A [label = '', shape = 'cisco.content_engine_(cache_director)']; }

     - shape = "cisco.multi-fabric_server_switch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.multi-fabric_server_switch']; }

     - shape = "cisco.content_switch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.content_switch']; }

   * - shape = "cisco.TP_MCU"

       .. blockdiag::

          { A [label = '', shape = 'cisco.TP_MCU']; }

     - shape = "cisco.MSE"

       .. blockdiag::

          { A [label = '', shape = 'cisco.MSE']; }

     - shape = "cisco.simulitlayer_switch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.simulitlayer_switch']; }

   * - shape = "cisco.accesspoint"

       .. blockdiag::

          { A [label = '', shape = 'cisco.accesspoint']; }

     - shape = "cisco.svx"

       .. blockdiag::

          { A [label = '', shape = 'cisco.svx']; }

     - shape = "cisco.softswitch_pgw_mgc"

       .. blockdiag::

          { A [label = '', shape = 'cisco.softswitch_pgw_mgc']; }

   * - shape = "cisco.10GE_FCoE"

       .. blockdiag::

          { A [label = '', shape = 'cisco.10GE_FCoE']; }

     - shape = "cisco.firewall_service_module_(fwsm)"

       .. blockdiag::

          { A [label = '', shape = 'cisco.firewall_service_module_(fwsm)']; }

     - shape = "cisco.icm"

       .. blockdiag::

          { A [label = '', shape = 'cisco.icm']; }

   * - shape = "cisco.content_service_switch_1100"

       .. blockdiag::

          { A [label = '', shape = 'cisco.content_service_switch_1100']; }

     - shape = "cisco.broadband_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.broadband_router']; }

     - shape = "cisco.itp"

       .. blockdiag::

          { A [label = '', shape = 'cisco.itp']; }

   * - shape = "cisco.hp_mini"

       .. blockdiag::

          { A [label = '', shape = 'cisco.hp_mini']; }

     - shape = "cisco.moh_server"

       .. blockdiag::

          { A [label = '', shape = 'cisco.moh_server']; }

     - shape = "cisco.generic_processor"

       .. blockdiag::

          { A [label = '', shape = 'cisco.generic_processor']; }

   * - shape = "cisco.pda"

       .. blockdiag::

          { A [label = '', shape = 'cisco.pda']; }

     - shape = "cisco.Nexus_1000"

       .. blockdiag::

          { A [label = '', shape = 'cisco.Nexus_1000']; }

     - shape = "cisco.general_applicance"

       .. blockdiag::

          { A [label = '', shape = 'cisco.general_applicance']; }

   * - shape = "cisco.Mediator"

       .. blockdiag::

          { A [label = '', shape = 'cisco.Mediator']; }

     - shape = "cisco.ciscosecurity"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ciscosecurity']; }

     - shape = "cisco.softphone"

       .. blockdiag::

          { A [label = '', shape = 'cisco.softphone']; }

   * - shape = "cisco.intelliswitch_stack"

       .. blockdiag::

          { A [label = '', shape = 'cisco.intelliswitch_stack']; }

     - shape = "cisco.radio_tower"

       .. blockdiag::

          { A [label = '', shape = 'cisco.radio_tower']; }

     - shape = "cisco.contact_center"

       .. blockdiag::

          { A [label = '', shape = 'cisco.contact_center']; }

   * - shape = "cisco.ibm_tower"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ibm_tower']; }

     - shape = "cisco.mulitswitch_device"

       .. blockdiag::

          { A [label = '', shape = 'cisco.mulitswitch_device']; }

     - shape = "cisco.standing_woman"

       .. blockdiag::

          { A [label = '', shape = 'cisco.standing_woman']; }

   * - shape = "cisco.pxf"

       .. blockdiag::

          { A [label = '', shape = 'cisco.pxf']; }

     - shape = "cisco.man_woman"

       .. blockdiag::

          { A [label = '', shape = 'cisco.man_woman']; }

     - shape = "cisco.terminal"

       .. blockdiag::

          { A [label = '', shape = 'cisco.terminal']; }

   * - shape = "cisco.service_control"

       .. blockdiag::

          { A [label = '', shape = 'cisco.service_control']; }

     - shape = "cisco.wlan_controller"

       .. blockdiag::

          { A [label = '', shape = 'cisco.wlan_controller']; }

     - shape = "cisco.pmc"

       .. blockdiag::

          { A [label = '', shape = 'cisco.pmc']; }

   * - shape = "cisco.phone_fax"

       .. blockdiag::

          { A [label = '', shape = 'cisco.phone_fax']; }

     - shape = "cisco.programmable_switch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.programmable_switch']; }

     - shape = "cisco.pc_man"

       .. blockdiag::

          { A [label = '', shape = 'cisco.pc_man']; }

   * - shape = "cisco.tape_array"

       .. blockdiag::

          { A [label = '', shape = 'cisco.tape_array']; }

     - shape = "cisco.mobile_access_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.mobile_access_router']; }

     - shape = "cisco.director-class_fibre_channel_director"

       .. blockdiag::

          { A [label = '', shape = 'cisco.director-class_fibre_channel_director']; }

   * - shape = "cisco.key"

       .. blockdiag::

          { A [label = '', shape = 'cisco.key']; }

     - shape = "cisco.running_man"

       .. blockdiag::

          { A [label = '', shape = 'cisco.running_man']; }

     - shape = "cisco.pad"

       .. blockdiag::

          { A [label = '', shape = 'cisco.pad']; }

   * - shape = "cisco.dslam"

       .. blockdiag::

          { A [label = '', shape = 'cisco.dslam']; }

     - shape = "cisco.detector"

       .. blockdiag::

          { A [label = '', shape = 'cisco.detector']; }

     - shape = "cisco.Ground_terminal"

       .. blockdiag::

          { A [label = '', shape = 'cisco.Ground_terminal']; }

   * - shape = "cisco.access_gateway"

       .. blockdiag::

          { A [label = '', shape = 'cisco.access_gateway']; }

     - shape = "cisco.ciscoworks"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ciscoworks']; }

     - shape = "cisco.netranger"

       .. blockdiag::

          { A [label = '', shape = 'cisco.netranger']; }

   * - shape = "cisco.adm"

       .. blockdiag::

          { A [label = '', shape = 'cisco.adm']; }

     - shape = "cisco.3200_mobile_access_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.3200_mobile_access_router']; }

     - shape = "cisco.workgroup_switch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.workgroup_switch']; }

   * - shape = "cisco.100baset_hub"

       .. blockdiag::

          { A [label = '', shape = 'cisco.100baset_hub']; }

     - shape = "cisco.cddi-fddi"

       .. blockdiag::

          { A [label = '', shape = 'cisco.cddi-fddi']; }

     - shape = "cisco.ACS"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ACS']; }

   * - shape = "cisco.telecommuter_house_pc"

       .. blockdiag::

          { A [label = '', shape = 'cisco.telecommuter_house_pc']; }

     - shape = "cisco.pbx"

       .. blockdiag::

          { A [label = '', shape = 'cisco.pbx']; }

     - shape = "cisco.gatekeeper"

       .. blockdiag::

          { A [label = '', shape = 'cisco.gatekeeper']; }

   * - shape = "cisco.handheld"

       .. blockdiag::

          { A [label = '', shape = 'cisco.handheld']; }

     - shape = "cisco.isdn_switch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.isdn_switch']; }

     - shape = "cisco.virtual_switch_controller_(vsc3000)"

       .. blockdiag::

          { A [label = '', shape = 'cisco.virtual_switch_controller_(vsc3000)']; }

   * - shape = "cisco.bbfw"

       .. blockdiag::

          { A [label = '', shape = 'cisco.bbfw']; }

     - shape = "cisco.ip_telephony_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ip_telephony_router']; }

     - shape = "cisco.router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.router']; }

   * - shape = "cisco.breakout_box"

       .. blockdiag::

          { A [label = '', shape = 'cisco.breakout_box']; }

     - shape = "cisco.centri_firewall"

       .. blockdiag::

          { A [label = '', shape = 'cisco.centri_firewall']; }

     - shape = "cisco.ip_phone"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ip_phone']; }

   * - shape = "cisco.ibm_mini_as400"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ibm_mini_as400']; }

     - shape = "cisco.wae"

       .. blockdiag::

          { A [label = '', shape = 'cisco.wae']; }

     - shape = "cisco.sattelite_dish"

       .. blockdiag::

          { A [label = '', shape = 'cisco.sattelite_dish']; }

   * - shape = "cisco.routerin_building"

       .. blockdiag::

          { A [label = '', shape = 'cisco.routerin_building']; }

     - shape = "cisco.androgenous_person"

       .. blockdiag::

          { A [label = '', shape = 'cisco.androgenous_person']; }

     - shape = "cisco.iptc"

       .. blockdiag::

          { A [label = '', shape = 'cisco.iptc']; }

   * - shape = "cisco.directory_server"

       .. blockdiag::

          { A [label = '', shape = 'cisco.directory_server']; }

     - shape = "cisco.generic_gateway"

       .. blockdiag::

          { A [label = '', shape = 'cisco.generic_gateway']; }

     - shape = "cisco.tv"

       .. blockdiag::

          { A [label = '', shape = 'cisco.tv']; }

   * - shape = "cisco.server_switch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.server_switch']; }

     - shape = "cisco.VSS"

       .. blockdiag::

          { A [label = '', shape = 'cisco.VSS']; }

     - shape = "cisco.host"

       .. blockdiag::

          { A [label = '', shape = 'cisco.host']; }

   * - shape = "cisco.keys"

       .. blockdiag::

          { A [label = '', shape = 'cisco.keys']; }

     - shape = "cisco.supercomputer"

       .. blockdiag::

          { A [label = '', shape = 'cisco.supercomputer']; }

     - shape = "cisco.wavelength_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.wavelength_router']; }

   * - shape = "cisco.ios_firewall"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ios_firewall']; }

     - shape = "cisco.wism"

       .. blockdiag::

          { A [label = '', shape = 'cisco.wism']; }

     - shape = "cisco.pc_software"

       .. blockdiag::

          { A [label = '', shape = 'cisco.pc_software']; }

   * - shape = "cisco.telecommuter_house"

       .. blockdiag::

          { A [label = '', shape = 'cisco.telecommuter_house']; }

     - shape = "cisco.storage_server"

       .. blockdiag::

          { A [label = '', shape = 'cisco.storage_server']; }

     - shape = "cisco.workgroup_director"

       .. blockdiag::

          { A [label = '', shape = 'cisco.workgroup_director']; }

   * - shape = "cisco.repeater"

       .. blockdiag::

          { A [label = '', shape = 'cisco.repeater']; }

     - shape = "cisco.MXE"

       .. blockdiag::

          { A [label = '', shape = 'cisco.MXE']; }

     - shape = "cisco.unity_server"

       .. blockdiag::

          { A [label = '', shape = 'cisco.unity_server']; }

   * - shape = "cisco.ace"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ace']; }

     - shape = "cisco.iptv_server"

       .. blockdiag::

          { A [label = '', shape = 'cisco.iptv_server']; }

     - shape = "cisco.end_office"

       .. blockdiag::

          { A [label = '', shape = 'cisco.end_office']; }

   * - shape = "cisco.cellular_phone"

       .. blockdiag::

          { A [label = '', shape = 'cisco.cellular_phone']; }

     - shape = "cisco.cable_modem"

       .. blockdiag::

          { A [label = '', shape = 'cisco.cable_modem']; }

     - shape = "cisco.diskette"

       .. blockdiag::

          { A [label = '', shape = 'cisco.diskette']; }

   * - shape = "cisco.cisco_unified_presence_server"

       .. blockdiag::

          { A [label = '', shape = 'cisco.cisco_unified_presence_server']; }

     - shape = "cisco.pbx_switch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.pbx_switch']; }

     - shape = "cisco.streamer"

       .. blockdiag::

          { A [label = '', shape = 'cisco.streamer']; }

   * - shape = "cisco.pix_firewall"

       .. blockdiag::

          { A [label = '', shape = 'cisco.pix_firewall']; }

     - shape = "cisco.Service_Module"

       .. blockdiag::

          { A [label = '', shape = 'cisco.Service_Module']; }

     - shape = "cisco.15200"

       .. blockdiag::

          { A [label = '', shape = 'cisco.15200']; }

   * - shape = "cisco.laptop"

       .. blockdiag::

          { A [label = '', shape = 'cisco.laptop']; }

     - shape = "cisco.stp"

       .. blockdiag::

          { A [label = '', shape = 'cisco.stp']; }

     - shape = "cisco.atm_tag_switch_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.atm_tag_switch_router']; }

   * - shape = "cisco.metro_1500"

       .. blockdiag::

          { A [label = '', shape = 'cisco.metro_1500']; }

     - shape = "cisco.csu_dsu"

       .. blockdiag::

          { A [label = '', shape = 'cisco.csu_dsu']; }

     - shape = "cisco.wireless_bridge"

       .. blockdiag::

          { A [label = '', shape = 'cisco.wireless_bridge']; }

   * - shape = "cisco.content_service_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.content_service_router']; }

     - shape = "cisco.Nexus_2000"

       .. blockdiag::

          { A [label = '', shape = 'cisco.Nexus_2000']; }

     - shape = "cisco.cisco_asa_5500"

       .. blockdiag::

          { A [label = '', shape = 'cisco.cisco_asa_5500']; }

   * - shape = "cisco.microphone"

       .. blockdiag::

          { A [label = '', shape = 'cisco.microphone']; }

     - shape = "cisco.atm_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.atm_router']; }

     - shape = "cisco.small_business"

       .. blockdiag::

          { A [label = '', shape = 'cisco.small_business']; }

   * - shape = "cisco.vpn_gateway"

       .. blockdiag::

          { A [label = '', shape = 'cisco.vpn_gateway']; }

     - shape = "cisco.atm_switch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.atm_switch']; }

     - shape = "cisco.rpsrps"

       .. blockdiag::

          { A [label = '', shape = 'cisco.rpsrps']; }

   * - shape = "cisco.router_with_silicon_switch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.router_with_silicon_switch']; }

     - shape = "cisco.jbod"

       .. blockdiag::

          { A [label = '', shape = 'cisco.jbod']; }

     - shape = "cisco.voice_switch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.voice_switch']; }

   * - shape = "cisco.ubr910"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ubr910']; }

     - shape = "cisco.csm-s"

       .. blockdiag::

          { A [label = '', shape = 'cisco.csm-s']; }

     - shape = "cisco.generic_building"

       .. blockdiag::

          { A [label = '', shape = 'cisco.generic_building']; }

   * - shape = "cisco.sattelite"

       .. blockdiag::

          { A [label = '', shape = 'cisco.sattelite']; }

     - shape = "cisco.dot-dot"

       .. blockdiag::

          { A [label = '', shape = 'cisco.dot-dot']; }

     - shape = "cisco.ibm_mainframe"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ibm_mainframe']; }

   * - shape = "cisco.Set_top_box"

       .. blockdiag::

          { A [label = '', shape = 'cisco.Set_top_box']; }

     - shape = "cisco.bridge"

       .. blockdiag::

          { A [label = '', shape = 'cisco.bridge']; }

     - shape = "cisco.cisco_ca"

       .. blockdiag::

          { A [label = '', shape = 'cisco.cisco_ca']; }

   * - shape = "cisco.web_browser"

       .. blockdiag::

          { A [label = '', shape = 'cisco.web_browser']; }

     - shape = "cisco.router_firewall"

       .. blockdiag::

          { A [label = '', shape = 'cisco.router_firewall']; }

     - shape = "cisco.h.323"

       .. blockdiag::

          { A [label = '', shape = 'cisco.h.323']; }

   * - shape = "cisco.firewall"

       .. blockdiag::

          { A [label = '', shape = 'cisco.firewall']; }

     - shape = "cisco.optical_transport"

       .. blockdiag::

          { A [label = '', shape = 'cisco.optical_transport']; }

     - shape = "cisco.wi-fi_tag"

       .. blockdiag::

          { A [label = '', shape = 'cisco.wi-fi_tag']; }

   * - shape = "cisco.avs"

       .. blockdiag::

          { A [label = '', shape = 'cisco.avs']; }

     - shape = "cisco.small_hub"

       .. blockdiag::

          { A [label = '', shape = 'cisco.small_hub']; }

     - shape = "cisco.fddi_ring"

       .. blockdiag::

          { A [label = '', shape = 'cisco.fddi_ring']; }

   * - shape = "cisco.workstation"

       .. blockdiag::

          { A [label = '', shape = 'cisco.workstation']; }

     - shape = "cisco.mobile_streamer"

       .. blockdiag::

          { A [label = '', shape = 'cisco.mobile_streamer']; }

     - shape = "cisco.Nexus_5000"

       .. blockdiag::

          { A [label = '', shape = 'cisco.Nexus_5000']; }

   * - shape = "cisco.video_camera"

       .. blockdiag::

          { A [label = '', shape = 'cisco.video_camera']; }

     - shape = "cisco.mcu"

       .. blockdiag::

          { A [label = '', shape = 'cisco.mcu']; }

     - shape = "cisco.ip_communicator"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ip_communicator']; }

   * - shape = "cisco.mobile_access_ip_phone"

       .. blockdiag::

          { A [label = '', shape = 'cisco.mobile_access_ip_phone']; }

     - shape = "cisco.ssc"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ssc']; }

     - shape = "cisco.mux"

       .. blockdiag::

          { A [label = '', shape = 'cisco.mux']; }

   * - shape = "cisco.microwebserver"

       .. blockdiag::

          { A [label = '', shape = 'cisco.microwebserver']; }

     - shape = "cisco.phone"

       .. blockdiag::

          { A [label = '', shape = 'cisco.phone']; }

     - shape = "cisco.Nexus_7000"

       .. blockdiag::

          { A [label = '', shape = 'cisco.Nexus_7000']; }

   * - shape = "cisco.sip_proxy_werver"

       .. blockdiag::

          { A [label = '', shape = 'cisco.sip_proxy_werver']; }

     - shape = "cisco.speaker"

       .. blockdiag::

          { A [label = '', shape = 'cisco.speaker']; }

     - shape = "cisco.university"

       .. blockdiag::

          { A [label = '', shape = 'cisco.university']; }

   * - shape = "cisco.mdu"

       .. blockdiag::

          { A [label = '', shape = 'cisco.mdu']; }

     - shape = "cisco.AXP"

       .. blockdiag::

          { A [label = '', shape = 'cisco.AXP']; }

     - shape = "cisco.tdm_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.tdm_router']; }

   * - shape = "cisco.cdm"

       .. blockdiag::

          { A [label = '', shape = 'cisco.cdm']; }

     - shape = "cisco.7500ars_(7513)"

       .. blockdiag::

          { A [label = '', shape = 'cisco.7500ars_(7513)']; }

     - shape = "cisco.asic_processor"

       .. blockdiag::

          { A [label = '', shape = 'cisco.asic_processor']; }

   * - shape = "cisco.Service_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.Service_router']; }

     - shape = "cisco.fc_storage"

       .. blockdiag::

          { A [label = '', shape = 'cisco.fc_storage']; }

     - shape = "cisco.mgx_8000_multiservice_switch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.mgx_8000_multiservice_switch']; }

   * - shape = "cisco.server_with_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.server_with_router']; }

     - shape = "cisco.pc_video"

       .. blockdiag::

          { A [label = '', shape = 'cisco.pc_video']; }

     - shape = "cisco.cisco_unityexpress"

       .. blockdiag::

          { A [label = '', shape = 'cisco.cisco_unityexpress']; }

   * - shape = "cisco.universal_gateway"

       .. blockdiag::

          { A [label = '', shape = 'cisco.universal_gateway']; }

     - shape = "cisco.cisco_1000"

       .. blockdiag::

          { A [label = '', shape = 'cisco.cisco_1000']; }

     - shape = "cisco.bts_10200"

       .. blockdiag::

          { A [label = '', shape = 'cisco.bts_10200']; }

   * - shape = "cisco.wireless"

       .. blockdiag::

          { A [label = '', shape = 'cisco.wireless']; }

     - shape = "cisco.pc_routercard"

       .. blockdiag::

          { A [label = '', shape = 'cisco.pc_routercard']; }

     - shape = "cisco.ata"

       .. blockdiag::

          { A [label = '', shape = 'cisco.ata']; }

   * - shape = "cisco.branch_office"

       .. blockdiag::

          { A [label = '', shape = 'cisco.branch_office']; }

     - shape = "cisco.NCE_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.NCE_router']; }

     - shape = "cisco.3174_(desktop)"

       .. blockdiag::

          { A [label = '', shape = 'cisco.3174_(desktop)']; }

   * - shape = "cisco.callmanager"

       .. blockdiag::

          { A [label = '', shape = 'cisco.callmanager']; }

     - shape = "cisco.class_4_5_switch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.class_4_5_switch']; }

     - shape = "cisco.RF_modem"

       .. blockdiag::

          { A [label = '', shape = 'cisco.RF_modem']; }

   * - shape = "cisco.pad_x.28"

       .. blockdiag::

          { A [label = '', shape = 'cisco.pad_x.28']; }

     - shape = "cisco.protocol_translator"

       .. blockdiag::

          { A [label = '', shape = 'cisco.protocol_translator']; }

     - shape = "cisco.NCE"

       .. blockdiag::

          { A [label = '', shape = 'cisco.NCE']; }

   * - shape = "cisco.optical_amplifier"

       .. blockdiag::

          { A [label = '', shape = 'cisco.optical_amplifier']; }

     - shape = "cisco.bbfw_media"

       .. blockdiag::

          { A [label = '', shape = 'cisco.bbfw_media']; }

     - shape = "cisco.nac_appliance"

       .. blockdiag::

          { A [label = '', shape = 'cisco.nac_appliance']; }

   * - shape = "cisco.cisco_hub"

       .. blockdiag::

          { A [label = '', shape = 'cisco.cisco_hub']; }

     - shape = "cisco.lightweight_ap"

       .. blockdiag::

          { A [label = '', shape = 'cisco.lightweight_ap']; }

     - shape = "cisco.telecommuter_icon"

       .. blockdiag::

          { A [label = '', shape = 'cisco.telecommuter_icon']; }

   * - shape = "cisco.wireless_transport"

       .. blockdiag::

          { A [label = '', shape = 'cisco.wireless_transport']; }

     - shape = "cisco.carrier_routing_system"

       .. blockdiag::

          { A [label = '', shape = 'cisco.carrier_routing_system']; }

     - shape = "cisco.hootphone"

       .. blockdiag::

          { A [label = '', shape = 'cisco.hootphone']; }

   * - shape = "cisco.content_switch_module"

       .. blockdiag::

          { A [label = '', shape = 'cisco.content_switch_module']; }

     - shape = "cisco.mas_gateway"

       .. blockdiag::

          { A [label = '', shape = 'cisco.mas_gateway']; }

     - shape = "cisco.vip"

       .. blockdiag::

          { A [label = '', shape = 'cisco.vip']; }

   * - shape = "cisco.wireless_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.wireless_router']; }

     - shape = "cisco.token"

       .. blockdiag::

          { A [label = '', shape = 'cisco.token']; }

     - shape = "cisco.cisco_file_engine"

       .. blockdiag::

          { A [label = '', shape = 'cisco.cisco_file_engine']; }

   * - shape = "cisco.longreach_cpe"

       .. blockdiag::

          { A [label = '', shape = 'cisco.longreach_cpe']; }

     - shape = "cisco.voice_atm_switch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.voice_atm_switch']; }

     - shape = "cisco.standing_man"

       .. blockdiag::

          { A [label = '', shape = 'cisco.standing_man']; }

   * - shape = "cisco.pc"

       .. blockdiag::

          { A [label = '', shape = 'cisco.pc']; }

     - shape = "cisco.atm_3800"

       .. blockdiag::

          { A [label = '', shape = 'cisco.atm_3800']; }

     - shape = "cisco.internet_streamer"

       .. blockdiag::

          { A [label = '', shape = 'cisco.internet_streamer']; }

   * - shape = "cisco.layer_3_switch"

       .. blockdiag::

          { A [label = '', shape = 'cisco.layer_3_switch']; }

     - shape = "cisco.bbsm"

       .. blockdiag::

          { A [label = '', shape = 'cisco.bbsm']; }

     - shape = "cisco.storage_router"

       .. blockdiag::

          { A [label = '', shape = 'cisco.storage_router']; }

   * - shape = "cisco.10700"

       .. blockdiag::

          { A [label = '', shape = 'cisco.10700']; }
     -
     -
