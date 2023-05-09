create_db = "CREATE DATABASE IF NOT EXISTS diploma"

create_cpus_table = """
    CREATE TABLE IF NOT EXISTS CPUS (
      id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
      name VARCHAR(255),
      price FLOAT,
      market_launch_date INT,
      lineup VARCHAR(255),
      delivery_type VARCHAR(255),
      cooling_included VARCHAR(255),
      crystal_code_name VARCHAR(255),
      socket VARCHAR(255),
      num_cores INT,
      max_threads INT,
      base_clock FLOAT,
      max_frequency FLOAT,
      l2_cache INT,
      l3_cache INT,
      memory_support VARCHAR(255),
      num_memory_channels INT,
      max_memory_without_overclocking INT,
      integrated_pcie_controller VARCHAR(255),
      pcie_controller_configuration VARCHAR(255),
      integrated_graphics VARCHAR(255),
      estimated_thermal_power FLOAT,
      process_technology INT,
      kernel_multithreading BOOLEAN,
      amd_v_virtualization BOOLEAN,
      vtx_intel_virtualization BOOLEAN,
      vtd_intel_virtualization BOOLEAN,
      intel_txt_secure_platform BOOLEAN
    );
"""

create_coolers_table = """
    CREATE TABLE IF NOT EXISTS COOLERS (
      id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
      name VARCHAR(255),
      price FLOAT,
      market_launch_date INT,
      cooler_type VARCHAR(255),
      cooling VARCHAR(255),
      color VARCHAR(255),
      socket VARCHAR(255),
      power_dissipation INT,
      radiator_material VARCHAR(255),
      num_heat_pipes VARCHAR(255),
      evaporation_chambers INT,
      fan_diameter INT,
      num_of_fans INT,
      bearing VARCHAR(255),
      minimum_rotation_speed INT,
      maximum_rotation_speed INT,
      max_airflow FLOAT,
      rotational_speed_control BOOLEAN,
      thermal_control BOOLEAN,
      connection_type VARCHAR(255),
      backlight_connection_type VARCHAR(255),
      led_backlight VARCHAR(255),
      vibration_isolation BOOLEAN,
      maximum_noise_level FLOAT,
      width INT,
      depth INT,
      height_or_thickness FLOAT,
      weight FLOAT,
      equipment VARCHAR(255)
    );
"""

create_motherboards_table = """
    CREATE TABLE IF NOT EXISTS MOTHERBOARDS (
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        name VARCHAR(255),
        price FLOAT,
        market_launch_date INT,
        processor_support VARCHAR(255),
        socket VARCHAR(255),
        chipset VARCHAR(255),
        form_factor VARCHAR(255),
        backlight BOOLEAN,
        memory_type VARCHAR(255),
        num_of_memory_slots INT,
        max_memory INT,
        memory_mode VARCHAR(255),
        max_memory_frequency INT,
        pci_express_version VARCHAR(255),
        total_pci_express_x16 VARCHAR(255),
        of_which_pci_express_2dot0_x16 VARCHAR(255),
        total_pci_express_x1 VARCHAR(255),
        of_which_pci_express_2dot0_x1 VARCHAR(255),
        total_pci_express_x4 VARCHAR(255),
        of_which_pci_express_2dot0_x4 VARCHAR(255),
        total_pci_express_x8 VARCHAR(255),
        of_which_pci_express_2dot0_x8 VARCHAR(255),
        pci VARCHAR(255),
        mdot2 VARCHAR(255),
        sata_3dot0 VARCHAR(255),
        sata_2dot0 VARCHAR(255),
        raid VARCHAR(255),
        slot_for_wifi_module VARCHAR(255),
        wifi VARCHAR(255),
        bluetooth VARCHAR(255),
        ethernet VARCHAR(255),
        integrated_graphics_support BOOLEAN,
        sli_or_crossfire_support VARCHAR(255),
        builtin_sound VARCHAR(255),
        sound_scheme VARCHAR(255),
        usb_2dot0_back_panel INT,
        usb_3dot2_gen1_type_a_5Gb_s_back_panel INT,
        usb_3dot2_gen2_type_a_10Gb_s_back_panel INT,
        usb_3dot2_gen1_type_c_5Gb_s_back_panel INT,
        usb_3dot2_gen2_type_c_10Gb_s_back_panel INT,
        usb_3dot2_gen2x2_20Gb_s_back_panel INT,
        usb_c_thunderbolt_3_back_panel INT,
        usb_c_thunderbolt_4_back_panel INT,
        s_or_pdif_digital_output INT,
        audio_3dot5_mm_jack INT,
        com_back_panel INT,
        lpt_back_panel INT,
        ps2 INT,
        display_port INT,
        mini_display_port INT,
        vga_or_dsub INT,
        dvi INT,
        hdmi INT,
        usb_2dot0_internal INT,
        usb_3dot2_gen1_type_a_5Gb_s_internal INT,
        usb_3dot2_gen2_type_a_10Gb_s_internal INT,
        usb_3dot2_gen1_type_c_5Gb_s_internal INT,
        usb_3dot2_gen2_type_c_10Gb_s_internal INT,
        usb_3dot2_gen2x2_20Gb_s_internal INT,
        thunderbolt3_internal INT,
        thunderbolt4_internal INT,
        s_or_pdif_digital_output_internal INT,
        com_internal INT,
        lpt_internal INT,
        cpu_fan_connectors INT,
        lss_connectors INT,
        case_fan_connectors INT,
        argb_5v_backlight_connectors INT,
        rgb_12v_backlight_connectors INT,
        builtin_connectors_description VARCHAR(2000),
        length FLOAT,
        width FLOAT
    );
"""

create_rams_table = """
    CREATE TABLE IF NOT EXISTS RAMS (
       id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
       name VARCHAR(255),
       price FLOAT,
       kit INTEGER,
       overall_volume INTEGER,
       one_module_volume INTEGER,
       ram_type VARCHAR(255),
       ecc VARCHAR(255),
       frequency INTEGER,
       pc_index VARCHAR(255),
       cas_latency VARCHAR(255),
       timings VARCHAR(255),
       supply_voltage FLOAT,
       xmp_profiles VARCHAR(255),
       amp_profiles VARCHAR(255),
       cooling BOOLEAN,
       low_profile_module BOOLEAN,
       board_elements_illumination BOOLEAN,
       color VARCHAR(255)
    );
"""

create_gpus_table = """
    CREATE TABLE IF NOT EXISTS GPUS (
      id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
      name VARCHAR(255),
      price FLOAT,
      market_launch_date INTEGER,
      gpu_description TEXT,
      selection_in_one_click TEXT,
      interface TEXT,
      gpu_manufacturer TEXT,
      microarchitecture TEXT,
      chip_code_name TEXT,
      gpu_overclocked_version BOOLEAN,
      ray_tracing BOOLEAN,
      mining_protection_or_lhr BOOLEAN,
      gpu_base_frequency INTEGER,
      max_gpu_frequency INTEGER,
      num_stream_processors INTEGER,
      num_rt_cores INTEGER,
      video_memory INTEGER,
      video_memory_type TEXT,
      effective_memory_frequency INTEGER,
      memory_bandwidth FLOAT,
      memory_bus_width INTEGER,
      directX_support TEXT,
      sli_or_crossfire_support TEXT,
      power_connectors VARCHAR(255),
      recommended_psu_watts INTEGER,
      cooling TEXT,
      cooling_system_thickness FLOAT,
      num_fans INTEGER,
      video_card_length FLOAT,
      video_card_height FLOAT,
      low_profile BOOLEAN,
      functional_features TEXT,
      vga_or_d_sub VARCHAR(50),
      dvi VARCHAR(50),
      hdmi VARCHAR(50),
      hdmi_version TEXT,
      mini_hdmi VARCHAR(50),
      display_port VARCHAR(50),
      display_port_version VARCHAR(50),
      mini_display_port VARCHAR(50),
      vesa_stereo VARCHAR(50),
      usb_type_c VARCHAR(50)
    );
"""

create_ssds_table = """
    CREATE TABLE IF NOT EXISTS SSDS (
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        name VARCHAR(255),
        price FLOAT,
        market_launch_date INT,
        ssd_description VARCHAR(2000),
        volume FLOAT,
        form_factor VARCHAR(255),
        interface VARCHAR(255),
        chip_type_flash VARCHAR(255),
        controller VARCHAR(255),
        m2_device_sizes VARCHAR(255),
        write_resource FLOAT,
        buffer_size VARCHAR(255),
        hardware_encryption VARCHAR(255),
        sequential_read_speed INT,
        sequential_write_speed INT,
        average_random_read_speed INT,
        average_random_write_speed INT,
        power_consumption_read_or_write FLOAT,
        power_consumption_cooling FLOAT,
        time_between_failures INT,
        thickness FLOAT,
        cooling BOOLEAN,
        backlight BOOLEAN,
        ps5_compatible BOOLEAN,
        delivery_option VARCHAR(2000),
        delivery_contents VARCHAR(2000),
        adapter_3dot5inch BOOLEAN
    );
"""

create_hhds_table = """
    CREATE TABLE IF NOT EXISTS HDDS (
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        name VARCHAR(255),
        price FLOAT,
        drive_type VARCHAR(255),
        volume FLOAT,
        form_factor VARCHAR(255),
        interface VARCHAR(255),
        spindle_speed INT,
        num_plates INT,
        buffer INT,
        hardware_encryption BOOLEAN,
        sector_size VARCHAR(255),
        sequential_read_speed INT,
        sequential_write_speed INT,
        noise_level_when_reading_or_writing INT,
        noise_level_in_standby_mode INT,
        shock_load_at_work INT,
        shock_load_in_non_operating_state INT,
        power_consumption_read_or_write FLOAT,
        power_consumption_standby FLOAT,
        time_between_failures INT,
        thickness FLOAT
    );
"""

create_powers_table = """
    CREATE TABLE IF NOT EXISTS POWERS (
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        name VARCHAR(255),
        price FLOAT,
        market_launch_date INT,
        power_description TEXT,
        purpose VARCHAR(255),
        power INT,
        power_supply_standard VARCHAR(255),
        input_voltage_range VARCHAR(255),
        number_of_individual_12v_lines INT,
        max_line_current_12v FLOAT,
        combined_12v_load FLOAT,
        power_factor_correction_efficiency VARCHAR(255),
        efficiency FLOAT,
        certificate_80plus VARCHAR(255),
        power_supply_fan_size INT,
        num_fans INT,
        fan_backlight BOOLEAN,
        case_backlight BOOLEAN,
        power_cable_length_12V FLOAT,
        modular_connection_power_cables BOOLEAN,
        motherboard_power VARCHAR(255),
        cpu_4pin VARCHAR(255),
        cpu_8pin VARCHAR(255),
        fdd_4pin VARCHAR(255),
        ide_4pin VARCHAR(255),
        sata VARCHAR(255),
        pcie_6pin VARCHAR(255),
        pcie_8pin VARCHAR(255),
        pcie_gen5_16pin VARCHAR(255),
        usb_power BOOLEAN,
        height FLOAT,
        width FLOAT,
        depth FLOAT,
        weight FLOAT,
        equipment TEXT
    );
"""

create_cases_table = """
    CREATE TABLE IF NOT EXISTS CASES (
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        name VARCHAR(255),
        price FLOAT,
        market_launch_date INT,
        power VARCHAR(255),
        case_description TEXT,
        case_type VARCHAR(255),
        case_for_games BOOLEAN,
        case_color VARCHAR(255),
        case_material VARCHAR(255),
        transparent_window BOOLEAN,
        window_material VARCHAR(255),
        case_front_panel VARCHAR(255),
        max_board_size VARCHAR(255),
        portable_power_supplies VARCHAR(255),
        power_supply_location VARCHAR(255),
        liquid_cooling_support BOOLEAN,
        supported_lss VARCHAR(1000),
        fans_included BOOLEAN,
        num_places_for_fans INT,
        installed_fans INT,
        fan_configuration TEXT,
        fan_light_color VARCHAR(255),
        noise_isolation BOOLEAN,
        bays_5dot25inch VARCHAR(255),
        external_3dot5_inch_bays VARCHAR(255),
        internal_3dot5_inch_bays VARCHAR(255),
        inch_bays_2dot5 VARCHAR(255),
        inch_combo_bay_2dot5_or_3dot5 VARCHAR(255),
        removable_drive_cage BOOLEAN,
        screwless_disc_mounting BOOLEAN,
        horizontal_expansion_slots VARCHAR(255),
        dust_filters BOOLEAN,
        case_illumination BOOLEAN,
        backlight_controller BOOLEAN,
        fan_rotation_controller BOOLEAN,
        video_card_holder BOOLEAN,
        max_graphics_card_length FLOAT,
        max_cpu_cooler_height FLOAT,
        max_power_supply_length FLOAT,
        vesa_mount BOOLEAN,
        door BOOLEAN,
        case_lock BOOLEAN,
        information_display BOOLEAN,
        usb_2dot0 VARCHAR(100),
        usb_3dot2_gen1_Type_a_or_5Gb_s VARCHAR(100),
        usb_3dot2_gen2_Type_a_or_10Gb_s VARCHAR(100),
        usb_3dot2_gen1_Type_c_or_5Gb_s VARCHAR(100),
        usb_3dot2_gen2_Type_c_or_10Gb_s VARCHAR(100),
        usb_3dot2_gen_2x2_or_20Gb_s VARCHAR(100),
        firewire VARCHAR(100),
        esata VARCHAR(100),
        docking_station_for_hard_drives VARCHAR(100),
        card_reader VARCHAR(100),
        audio_output VARCHAR(100),
        microphone_input VARCHAR(100),
        height FLOAT,
        width FLOAT,
        depth FLOAT,
        weight FLOAT
    );
"""

create_configuration_table = """
    CREATE TABLE IF NOT EXISTS CONFIGURATION (
      id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
      cpu_id INT,
      cooler_id INT,
      motherboard_id INT,
      ram_id INT,
      gpu_id INT,
      ssd_id INT,
      hdd_id INT,
      power_id INT,
      case_id INT,
      FOREIGN KEY (cpu_id) REFERENCES CPU(id),
      FOREIGN KEY (cooler_id) REFERENCES COOLER(id),
      FOREIGN KEY (motherboard_id) REFERENCES MOTHERBOARD(id),
      FOREIGN KEY (ram_id) REFERENCES RAM(id),
      FOREIGN KEY (gpu_id) REFERENCES GPU(id),
      FOREIGN KEY (ssd_id) REFERENCES SSD(id),
      FOREIGN KEY (hdd_id) REFERENCES HDD(id),
      FOREIGN KEY (power_id) REFERENCES POWER(id),
      FOREIGN KEY (case_id) REFERENCES CASE(id)
    );
"""