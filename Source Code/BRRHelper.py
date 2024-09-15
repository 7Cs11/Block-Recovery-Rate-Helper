import os
import binascii
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QHBoxLayout, QPushButton, QFileDialog, QHeaderView
from PyQt5.QtGui import QPixmap

class MainGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Block-Recovery Rate Helper')
        self.setGeometry(100, 100, 2400, 1800)

        self.button = QPushButton('Open Save File', self)
        self.button.clicked.connect(self.openFileExplorer)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def openFileExplorer(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select a File")
        if file_path:
            self.analyze_file(file_path)

    def analyze_file(self, directory):
        
        collected_block_list = []

        with open(directory, 'rb') as file:

            ##### Reads the byte and converts it to binary #####
            def process_byte(byte_location):
                file.seek(byte_location) 
                byte = file.read(1)
                byte = bin(byte[0])[2:].zfill(8)
                return byte
            #####
            
            ##### Pi'illo Blimport #####
            PilloBlimp_number_collected = 12
            total_blocks_collected = 681

            PilloBlimp_list = [
                [0x0B8, 0, "PilloBlimp_1"],
                [0x0B9, 7, "PilloBlimp_2"],
                [0x0B9, 6, "PilloBlimp_3"],
                [0x0B9, 5, "PilloBlimp_4"],
                [0x0B9, 4, "PilloBlimp_5"],
                [0x0B9, 3, "PilloBlimp_6"],
                [0x0B9, 2, "PilloBlimp_7"],
                [0x0B9, 1, "PilloBlimp_8"],
                [0x0B9, 0, "PilloBlimp_9"],
                [0x0BA, 4, "PilloBlimp_10"],
                [0x333, 1, "PilloBlimp_11"],
                [0x0BA, 6, "PilloBlimp_12"],
            ]

            for block_list in PilloBlimp_list:
                (byte_location, bit, name) = block_list
                byte = process_byte(byte_location)
                if byte[bit] != '1':
                    collected_block_list.append([name, "PilloBlimp", "Pi'illo Blimport"])
                    PilloBlimp_number_collected -= 1
                    total_blocks_collected -= 1

            #### Pi'illo Castle ####
            PilloCastle_number_collected = 30
                       
            PilloCastle_list = [
                    [0x0BB, 7, "PilloCastle_1"],
                    [0x0BB, 6, "PilloCastle_2"],
                    [0x1E2, 7, "PilloCastle_3"],
                    [0x1E2, 5, "PilloCastle_4"],
                    [0x1E2, 4, "PilloCastle_5"],
                    [0x1E2, 6, "PilloCastle_6"],
                    [0x0BC, 6, "PilloCastle_7"],
                    [0x0BB, 5, "PilloCastle_8"],
                    [0x0BB, 3, "PilloCastle_9"],
                    [0x0BB, 1, "PilloCastle_10"],
                    [0x0BB, 2, "PilloCastle_11"],
                    [0x0BC, 4, "PilloCastle_12"],
                    [0x0BD, 6, "PilloCastle_13"],
                    [0x0BD, 5, "PilloCastle_14"],
                    [0x0BD, 4, "PilloCastle_15"],
                    [0x408, 3, "PilloCastle_16"],
                    [0x1E1, 0, "PilloCastle_17"],
                    [0x0BD, 2, "PilloCastle_18"],
                    [0x0BD, 0, "PilloCastle_19"],
                    [0x333, 0, "PilloCastle_20"],
                    [0x0BD, 1, "PilloCastle_21"],
                    [0x0BC, 5, "PilloCastle_22"],
                    [0x0BB, 0, "PilloCastle_23"],
                    [0x0BC, 7, "PilloCastle_24"],
                    [0x0BB, 4, "PilloCastle_25"],
                    [0x0BC, 2, "PilloCastle_26"],
                    [0x0BC, 1, "PilloCastle_27"],
                    [0x0BD, 7, "PilloCastle_28"],
                    [0x0BC, 0, "PilloCastle_29"],
                    [0x0BC, 3, "PilloCastle_30"],
                ];
             
            for block_list in PilloCastle_list:
                (byte_location, bit, name) = block_list
                byte = process_byte(byte_location)
                if byte[bit] != '1':
                    collected_block_list.append([name, "PilloCastle", "Pi'illo Castle"])
                    total_blocks_collected -= 1
                    PilloCastle_number_collected -= 1

             #### Mushrise Park ####
            MushPark_number_collected = 50
            
            MushPark_list = [
                    [0x0BF, 5, "MushPark_1"],
                    [0x0BF, 7, "MushPark_2"],
                    [0x0BF, 6, "MushPark_3"],
                    [0x0C2, 7, "MushPark_4"],
                    [0x0BF, 0, "MushPark_5"],
                    [0x0BF, 1, "MushPark_6"],
                    [0x0BE, 1, "MushPark_7"],
                    [0x0C0, 7, "MushPark_8"],
                    [0x0C0, 6, "MushPark_9"],
                    [0x0C0, 3, "MushPark_10"],
                    [0x0C0, 1, "MushPark_11"],
                    [0x0C0, 0, "MushPark_12"],
                    [0x3A3, 1, "MushPark_13"],
                    [0x0C0, 2, "MushPark_14"],
                    [0x0C0, 5, "MushPark_15"],
                    [0x0C6, 7, "MushPark_16"],
                    [0x0C6, 6, "MushPark_17"],
                    [0x0C6, 5, "MushPark_18"],
                    [0x0C1, 6, "MushPark_19"],
                    [0x0C1, 7, "MushPark_20"],
                    [0x0C2, 6, "MushPark_21"],
                    [0x0C1, 0, "MushPark_22"],
                    [0x0C1, 1, "MushPark_23"],
                    [0x0C3, 4, "MushPark_24"],
                    [0x399, 2, "MushPark_25"],
                    [0x0BE, 0, "MushPark_26"],
                    [0x3A3, 0, "MushPark_27"],
                    [0x3D1, 6, "MushPark_28"],
                    [0x0C6, 4, "MushPark_29"],
                    [0x0C5, 4, "MushPark_30"],
                    [0x0C4, 0, "MushPark_31"],
                    [0x0C5, 7, "MushPark_32"],
                    [0x1E2, 0, "MushPark_33"],
                    [0x1E2, 1, "MushPark_34"],
                    [0x0C1, 5, "MushPark_35"],
                    [0x0C6, 2, "MushPark_36"],
                    [0x0C3, 7, "MushPark_37"],
                    [0x0C2, 0, "MushPark_38"],
                    [0x0C2, 1, "MushPark_39"],
                    [0x0C3, 6, "MushPark_40"],
                    [0x0BE, 3, "MushPark_41"],
                    [0x0BE, 2, "MushPark_42"],
                    [0x0C3, 3, "MushPark_43"],
                    [0x0C4, 6, "MushPark_44"],
                    [0x0C4, 7, "MushPark_45"],
                    [0x0C3, 1, "MushPark_46"],
                    [0x1E2, 2, "MushPark_47"],
                    [0x0C4, 5, "MushPark_48"],
                    [0x0C3, 0, "MushPark_49"],
                    [0x0C6, 3, "MushPark_50"],
                ];
             
            for block_list in MushPark_list:
                (byte_location, bit, name) = block_list
                byte = process_byte(byte_location)
                if byte[bit] != '1':
                    collected_block_list.append([name, "MushPark", "Mushrise Park"])
                    total_blocks_collected -= 1
                    MushPark_number_collected -= 1

            #### Dozing Sands ####
            DozSands_number_collected = 61
                       
            DozSands_list = [
                    [0x2ED, 7, "DozSands_1"],
                    [0x0D9, 2, "DozSands_2"],
                    [0x0D9, 1, "DozSands_3"],
                    [0x0D8, 5, "DozSands_4"],
                    [0x0D8, 7, "DozSands_5"],
                    [0x0D8, 6, "DozSands_6"],
                    [0x0DB, 2, "DozSands_7"],
                    [0x0DB, 5, "DozSands_8"],
                    [0x2DF, 7, "DozSands_9"],
                    [0x2ED, 1, "DozSands_10"],
                    [0x0DB, 4, "DozSands_11"],
                    [0x0D9, 4, "DozSands_12"],
                    [0x0DA, 2, "DozSands_13"],
                    [0x0DA, 1, "DozSands_14"],
                    [0x0DD, 3, "DozSands_15"],
                    [0x0DD, 2, "DozSands_16"],
                    [0x0DE, 1, "DozSands_17"],
                    [0x0DE, 0, "DozSands_18"],
                    [0x0DF, 7, "DozSands_19"],
                    [0x0DB, 0, "DozSands_20"],
                    [0x0DC, 7, "DozSands_21"],
                    [0x0DC, 6, "DozSands_22"],
                    [0x0DC, 4, "DozSands_23"],
                    [0x0DC, 4, "DozSands_24"],
                    [0x0DE, 2, "DozSands_25"],
                    [0x0DC, 2, "DozSands_26"],
                    [0x1E0, 2, "DozSands_27"],
                    [0x0DD, 0, "DozSands_28"],
                    [0x0DE, 6, "DozSands_29"],
                    [0x0DE, 5, "DozSands_30"],
                    [0x0DE, 7, "DozSands_31"],
                    [0x0DD, 1, "DozSands_32"],
                    [0x0DA, 0, "DozSands_33"],
                    [0x0DA, 5, "DozSands_34"],
                    [0x0DA, 6, "DozSands_35"],
                    [0x0E2, 6, "DozSands_36"],
                    [0x0E2, 7, "DozSands_37"],
                    [0x0E1, 0, "DozSands_38"],
                    [0x0E1, 1, "DozSands_39"],
                    [0x0E1, 2, "DozSands_40"],
                    [0x0D8, 3, "DozSands_41"],
                    [0x2ED, 5, "DozSands_42"],
                    [0x30F, 4, "DozSands_43"],
                    [0x0DF, 3, "DozSands_44"],
                    [0x0DF, 4, "DozSands_45"],
                    [0x0D9, 5, "DozSands_46"],
                    [0x0D7, 0, "DozSands_47"],
                    [0x1E0, 1, "DozSands_48"],
                    [0x0DE, 3, "DozSands_49"],
                    [0x0DF, 1, "DozSands_50"],
                    [0x0DF, 6, "DozSands_51"],
                    [0x0DF, 5, "DozSands_52"],
                    [0x0D8, 1, "DozSands_53"],
                    [0x0D8, 2, "DozSands_54"],
                    [0x0DF, 0, "DozSands_55"],
                    [0x0E0, 7, "DozSands_56"],
                    [0x0E0, 3, "DozSands_57"],
                    [0x0E0, 4, "DozSands_58"],
                    [0x1E3, 3, "DozSands_59"],
                    [0x0E0, 1, "DozSands_60"],
                    [0x0E0, 2, "DozSands_61"],
                ];

            for block_list in DozSands_list:
                (byte_location, bit, name) = block_list
                byte = process_byte(byte_location)
                if byte[bit] != '1':
                    collected_block_list.append([name, "DozSands", "Dozing Sands"])
                    total_blocks_collected -= 1
                    DozSands_number_collected -= 1

            #### Wakeport ####
            Wakeport_number_collected = 33
                       
            Wakeport_list = [
                    [0x174, 5, "Wakeport_1"],
                    [0x3D1, 5, "Wakeport_2"],
                    [0x178, 3, "Wakeport_3"],
                    [0x3D1, 4, "Wakeport_4"],
                    [0x178, 2, "Wakeport_5"],
                    [0x175, 5, "Wakeport_6"],
                    [0x176, 4, "Wakeport_7"],
                    [0x175, 0, "Wakeport_8"],
                    [0x3A6, 3, "Wakeport_9"],
                    [0x178, 1, "Wakeport_10"],
                    [0x177, 6, "Wakeport_11"],
                    [0x177, 3, "Wakeport_12"],
                    [0x176, 0, "Wakeport_13"],
                    [0x177, 7, "Wakeport_14"],
                    [0x177, 4, "Wakeport_15"],
                    [0x177, 5, "Wakeport_16"],
                    [0x176, 2, "Wakeport_17"],
                    [0x176, 3, "Wakeport_18"],
                    [0x176, 5, "Wakeport_19"],
                    [0x3A6, 5, "Wakeport_20"],
                    [0x176, 1, "Wakeport_21"],
                    [0x3A6, 4, "Wakeport_22"],
                    [0x174, 4, "Wakeport_23"],
                    [0x174, 0, "Wakeport_24"],
                    [0x178, 4, "Wakeport_25"],
                    [0x174, 2, "Wakeport_26"],
                    [0x174, 3, "Wakeport_27"],
                    [0x177, 2, "Wakeport_28"],
                    [0x177, 1, "Wakeport_29"],
                    [0x178, 6, "Wakeport_30"],
                    [0x178, 5, "Wakeport_31"],
                    [0x178, 7, "Wakeport_32"],
                    [0x177, 0, "Wakeport_33"],
                ];
             
            for block_list in Wakeport_list:
                (byte_location, bit, name) = block_list
                byte = process_byte(byte_location)
                if byte[bit] != '1':
                    collected_block_list.append([name, "Wakeport", "Wakeport"])
                    total_blocks_collected -= 1
                    Wakeport_number_collected -= 1

            #### Mount Pajamaja ####
            MountPaj_number_collected = 47
             
            MountPaj_list = [
                    [0x17C, 2, "MountPaj_1"],
                    [0x17C, 0, "MountPaj_2"],
                    [0x17C, 1, "MountPaj_3"],
                    [0x17D, 7, "MountPaj_4"],
                    [0x17D, 6, "MountPaj_5"],
                    [0x17D, 2, "MountPaj_6"],
                    [0x17E, 1, "MountPaj_7"],
                    [0x17E, 3, "MountPaj_8"],
                    [0x17E, 2, "MountPaj_9"],
                    [0x17D, 1, "MountPaj_10"],
                    [0x17E, 7, "MountPaj_11"],
                    [0x17E, 5, "MountPaj_12"],
                    [0x17D, 5, "MountPaj_13"],
                    [0x17E, 4, "MountPaj_14"],
                    [0x17F, 7, "MountPaj_15"],
                    [0x17F, 3, "MountPaj_16"],
                    [0x17F, 2, "MountPaj_17"],
                    [0x1DB, 2, "MountPaj_18"],
                    [0x179, 5, "MountPaj_19"],
                    [0x1CD, 4, "MountPaj_20"],
                    [0x1E4, 4, "MountPaj_21"],
                    [0x30F, 3, "MountPaj_22"],
                    [0x180, 5, "MountPaj_23"],
                    [0x30F, 2, "MountPaj_24"],
                    [0x180, 3, "MountPaj_25"],
                    [0x181, 5, "MountPaj_26"],
                    [0x1E0, 0, "MountPaj_27"],
                    [0x181, 6, "MountPaj_28"],
                    [0x181, 7, "MountPaj_29"],
                    [0x181, 1, "MountPaj_30"],
                    [0x182, 7, "MountPaj_31"],
                    [0x182, 6, "MountPaj_32"],
                    [0x180, 1, "MountPaj_33"],
                    [0x181, 0, "MountPaj_34"],
                    [0x17F, 4, "MountPaj_35"],
                    [0x180, 4, "MountPaj_36"],
                    [0x17F, 0, "MountPaj_37"],
                    [0x17F, 1, "MountPaj_38"],
                    [0x182, 2, "MountPaj_39"],
                    [0x182, 0, "MountPaj_40"],
                    [0x183, 7, "MountPaj_41"],
                    [0x1E4, 3, "MountPaj_42"],
                    [0x181, 4, "MountPaj_43"],
                    [0x181, 3, "MountPaj_44"],
                    [0x183, 5, "MountPaj_45"],
                    [0x183, 6, "MountPaj_46"],
                    [0x183, 4, "MountPaj_47"],
                ];
             
            for block_list in MountPaj_list:
                (byte_location, bit, name) = block_list
                byte = process_byte(byte_location)
                if byte[bit] != '1':
                    collected_block_list.append([name, "MountPaj", "Mount Pajamaja"])
                    total_blocks_collected -= 1
                    MountPaj_number_collected -= 1

            #### Driftwood Shore ####
            DriftShore_number_collected = 30
         
            DriftShore_list = [
                    [0x405, 7, "DriftShore_1"],
                    [0x179, 7, "DriftShore_2"],
                    [0x179, 6, "DriftShore_3"],
                    [0x178, 0, "DriftShore_4"],
                    [0x1E3, 1, "DriftShore_5"],
                    [0x179, 4, "DriftShore_6"],
                    [0x1E3, 0, "DriftShore_7"],
                    [0x179, 1, "DriftShore_8"],
                    [0x179, 2, "DriftShore_9"],
                    [0x179, 0, "DriftShore_10"],
                    [0x17A, 6, "DriftShore_11"],
                    [0x17A, 5, "DriftShore_12"],
                    [0x1DB, 3, "DriftShore_13"],
                    [0x1DB, 4, "DriftShore_14"],
                    [0x17A, 1, "DriftShore_15"],
                    [0x17A, 4, "DriftShore_16"],
                    [0x17A, 3, "DriftShore_17"],
                    [0x17A, 0, "DriftShore_18"],
                    [0x17B, 3, "DriftShore_19"],
                    [0x17B, 4, "DriftShore_20"],
                    [0x334, 7, "DriftShore_21"],
                    [0x17B, 5, "DriftShore_22"],
                    [0x407, 2, "DriftShore_23"],
                    [0x407, 3, "DriftShore_24"],
                    [0x17B, 7, "DriftShore_25"],
                    [0x17B, 1, "DriftShore_26"],
                    [0x17C, 6, "DriftShore_27"],
                    [0x17C, 7, "DriftShore_28"],
                    [0x17B, 0, "DriftShore_29"],
                    [0x17C, 5, "DriftShore_30"],
                ];
             
            for block_list in DriftShore_list:
                (byte_location, bit, name) = block_list
                byte = process_byte(byte_location)
                if byte[bit] != '1':
                    collected_block_list.append([name, "DriftShore", "Driftwood Shores"])
                    total_blocks_collected -= 1
                    DriftShore_number_collected -= 1

            #### Somnom Woods ####
            SomWoods_number_collected = 33
        
            SomWoods_list = [
                    [0x1BD, 3, "SomWoods_1"],
                    [0x1BD, 0, "SomWoods_2"],
                    [0x1BD, 1, "SomWoods_3"],
                    [0x1BE, 6, "SomWoods_4"],
                    [0x1BE, 5, "SomWoods_5"],
                    [0x334, 6, "SomWoods_6"],
                    [0x1BE, 4, "SomWoods_7"],
                    [0x1BE, 3, "SomWoods_8"],
                    [0x1BE, 0, "SomWoods_9"],
                    [0x1BF, 7, "SomWoods_10"],
                    [0x1BE, 1, "SomWoods_11"],
                    [0x1BF, 6, "SomWoods_12"],
                    [0x1BF, 3, "SomWoods_13"],
                    [0x1BF, 2, "SomWoods_14"],
                    [0x1C1, 7, "SomWoods_15"],
                    [0x1BF, 1, "SomWoods_16"],
                    [0x1BF, 0, "SomWoods_17"],
                    [0x334, 5, "SomWoods_18"],
                    [0x1C0, 6, "SomWoods_19"],
                    [0x1C0, 3, "SomWoods_20"],
                    [0x1C0, 4, "SomWoods_21"],
                    [0x1C0, 5, "SomWoods_22"],
                    [0x1C1, 6, "SomWoods_23"],
                    [0x334, 4, "SomWoods_24"],
                    [0x1C0, 0, "SomWoods_25"],
                    [0x1C1, 5, "SomWoods_26"],
                    [0x1C1, 1, "SomWoods_27"],
                    [0x1C1, 2, "SomWoods_28"],
                    [0x332, 2, "SomWoods_29"],
                    [0x1C2, 7, "SomWoods_30"],
                    [0x1C2, 6, "SomWoods_31"],
                    [0x1C2, 5, "SomWoods_32"],
                    [0x1C2, 4, "SomWoods_33"],
                ];
             
            for block_list in SomWoods_list:
                (byte_location, bit, name) = block_list
                byte = process_byte(byte_location)
                if byte[bit] != '1':
                    collected_block_list.append([name, "SomWoods", "Somnom Woods"])
                    total_blocks_collected -= 1
                    SomWoods_number_collected -=1

            #### Neo Bowser Castle ####
            NBC_number_collected = 59
         
            NBC_list = [
                    [0x184, 7, "NBC_1"],
                    [0x184, 6, "NBC_2"],
                    [0x183, 1, "NBC_3"],
                    [0x183, 0, "NBC_4"],
                    [0x184, 4, "NBC_5"],
                    [0x184, 5, "NBC_6"],
                    [0x184, 1, "NBC_7"],
                    [0x184, 2, "NBC_8"],
                    [0x184, 3, "NBC_9"],
                    [0x0DB, 7, "NBC_10"],
                    [0x0E0, 5, "NBC_11"],
                    [0x185, 5, "NBC_12"],
                    [0x1DF, 3, "NBC_13"],
                    [0x1DF, 4, "NBC_14"],
                    [0x1DF, 0, "NBC_15"],
                    [0x1DF, 1, "NBC_16"],
                    [0x1E4, 2, "NBC_17"],
                    [0x185, 1, "NBC_18"],
                    [0x185, 0, "NBC_19"],
                    [0x1E4, 1, "NBC_20"],
                    [0x1E4, 0, "NBC_21"],
                    [0x1DF, 2, "NBC_22"],
                    [0x186, 3, "NBC_23"],
                    [0x1D7, 6, "NBC_24"],
                    [0x1D7, 5, "NBC_25"],
                    [0x186, 4, "NBC_26"],
                    [0x186, 1, "NBC_27"],
                    [0x186, 2, "NBC_28"],
                    [0x1E0, 6, "NBC_29"],
                    [0x1E1, 7, "NBC_30"],
                    [0x1E0, 7, "NBC_31"],
                    [0x187, 5, "NBC_32"],
                    [0x186, 0, "NBC_33"],
                    [0x30F, 1, "NBC_34"],
                    [0x188, 7, "NBC_35"],
                    [0x1E1, 3, "NBC_36"],
                    [0x1E1, 2, "NBC_37"],
                    [0x187, 0, "NBC_38"],
                    [0x309, 3, "NBC_39"],
                    [0x30C, 3, "NBC_40"],
                    [0x187, 2, "NBC_41"],
                    [0x30B, 2, "NBC_42"],
                    [0x187, 7, "NBC_43"],
                    [0x187, 6, "NBC_44"],
                    [0x1E1, 6, "NBC_45"],
                    [0x1E1, 5, "NBC_46"],
                    [0x30B, 1, "NBC_47"],
                    [0x30B, 0, "NBC_48"],
                    [0x188, 5, "NBC_49"],
                    [0x188, 6, "NBC_50"],
                    [0x188, 1, "NBC_51"],
                    [0x188, 0, "NBC_52"],
                    [0x188, 4, "NBC_53"],
                    [0x310, 7, "NBC_54"],
                    [0x189, 4, "NBC_55"],
                    [0x189, 6, "NBC_56"],
                    [0x189, 5, "NBC_57"],
                    [0x189, 7, "NBC_58"],
                    [0x30F, 0, "NBC_59"],
                ];
             
            for block_list in NBC_list:
                (byte_location, bit, name) = block_list
                byte = process_byte(byte_location)
                if byte[bit] != '1':
                    collected_block_list.append([name, "NBC", "Neo Bowser Castle"])
                    total_blocks_collected -= 1
                    NBC_number_collected -= 1

            #### Dreamy Pi'illo Castle ####
            D_PilloCastle_number_collected = 52
     
            D_PilloCastle_list = [
                    [0x0CB, 2, "D_PilloCastle_1"],
                    [0x0CB, 0, "D_PilloCastle_2"],
                    [0x0CB, 1, "D_PilloCastle_3"],
                    [0x0CC, 2, "D_PilloCastle_4"],
                    [0x0CC, 4, "D_PilloCastle_5"],
                    [0x0CC, 3, "D_PilloCastle_6"],
                    [0x0CC, 6, "D_PilloCastle_7"],
                    [0x0CC, 5, "D_PilloCastle_8"],
                    [0x123, 1, "D_PilloCastle_9"],
                    [0x123, 2, "D_PilloCastle_10"],
                    [0x0D5, 6, "D_PilloCastle_11"],
                    [0x0D5, 1, "D_PilloCastle_12"],
                    [0x0D5, 2, "D_PilloCastle_13"],
                    [0x0D5, 3, "D_PilloCastle_14"],
                    [0x0D5, 4, "D_PilloCastle_15"],
                    [0x0D6, 2, "D_PilloCastle_16"],
                    [0x0D6, 1, "D_PilloCastle_17"],
                    [0x0CC, 1, "D_PilloCastle_18"],
                    [0x185, 4, "D_PilloCastle_19"],
                    [0x0CD, 7, "D_PilloCastle_20"],
                    [0x0CD, 6, "D_PilloCastle_21"],
                    [0x0CD, 4, "D_PilloCastle_22"],
                    [0x0CD, 2, "D_PilloCastle_23"],
                    [0x0CD, 0, "D_PilloCastle_24"],
                    [0x0CE, 6, "D_PilloCastle_25"],
                    [0x0D0, 6, "D_PilloCastle_26"],
                    [0x0CF, 5, "D_PilloCastle_27"],
                    [0x0CF, 2, "D_PilloCastle_28"],
                    [0x0CF, 0, "D_PilloCastle_29"],
                    [0x0D0, 6, "D_PilloCastle_30"],
                    [0x0D0, 4, "D_PilloCastle_31"],
                    [0x0D0, 2, "D_PilloCastle_32"],
                    [0x0D0, 0, "D_PilloCastle_33"],
                    [0x0D1, 6, "D_PilloCastle_34"],
                    [0x0CF, 3, "D_PilloCastle_35"],
                    [0x0CF, 4, "D_PilloCastle_36"],
                    [0x0D2, 2, "D_PilloCastle_37"],
                    [0x0D2, 0, "D_PilloCastle_38"],
                    [0x0D3, 6, "D_PilloCastle_39"],
                    [0x0D3, 4, "D_PilloCastle_40"],
                    [0x0D3, 2, "D_PilloCastle_41"],
                    [0x0D3, 0, "D_PilloCastle_42"],
                    [0x0D4, 6, "D_PilloCastle_43"],
                    [0x0D4, 5, "D_PilloCastle_44"],
                    [0x0D4, 2, "D_PilloCastle_45"],
                    [0x0D4, 0, "D_PilloCastle_46"],
                    [0x0D1, 4, "D_PilloCastle_47"],
                    [0x0D1, 2, "D_PilloCastle_48"],
                    [0x0D1, 0, "D_PilloCastle_49"],
                    [0x0D2, 6, "D_PilloCastle_50"],
                    [0x0D2, 4, "D_PilloCastle_51"],
                    [0x0CF, 7, "D_PilloCastle_52"],
                ];

            for block_list in D_PilloCastle_list:
                (byte_location, bit, name) = block_list
                byte = process_byte(byte_location)
                if byte[bit] != '1':
                    if any(name.endswith(f"{i}") for i in range(1, 9)):
                        location = "Prince Dreambert Dreampoint"

                    if any(name.endswith(f"{i}") for i in range(9, 11)):
                        location = "Dream's Deep"
                    
                    if any(name.endswith(f"{i}") for i in range(11, 18)):
                        location = "Pink Pi'illo Dream World in Pi'illo Castle Underground"
                    
                    if any(name.endswith(f"{i}") for i in range(18, 26)):
                        location = "First Blue Pi'illo Dream World in Pi'illo Castle Underground"

                    if any(name.endswith(f"{i}") for i in range(26, 53)):
                        location = "Second Blue Pi'illo Dream World in Pi'illo Castle Underground"

                    collected_block_list.append([name, "D_PilloCastle", location])
                    total_blocks_collected -= 1
                    D_PilloCastle_number_collected -= 1

            #### Dreamy Mushrise Park ####
            D_MushPark_number_collected = 21
     
            D_MushPark_list = [
                    [0x0CB, 7, "D_MushPark_1"],
                    [0x0C7, 6, "D_MushPark_2"],
                    [0x0C6, 0, "D_MushPark_3"],
                    [0x0C7, 2, "D_MushPark_4"],
                    [0x0C7, 4, "D_MushPark_5"],
                    [0x0C7, 0, "D_MushPark_6"],
                    [0x0C8, 6, "D_MushPark_7"],
                    [0x0CA, 7, "D_MushPark_8"],
                    [0x1E3, 6, "D_MushPark_9"],
                    [0x0CA, 6, "D_MushPark_10"],
                    [0x0CA, 5, "D_MushPark_11"],
                    [0x0CA, 4, "D_MushPark_12"],
                    [0x0C9, 1, "D_MushPark_13"],
                    [0x0C9, 2, "D_MushPark_14"],
                    [0x0C8, 4, "D_MushPark_15"],
                    [0x1E3, 7, "D_MushPark_16"],
                    [0x0C8, 3, "D_MushPark_17"],
                    [0x0CA, 2, "D_MushPark_18"],
                    [0x1E3, 4, "D_MushPark_19"],
                    [0x1E3, 5, "D_MushPark_20"],
                    [0x0CA, 0, "D_MushPark_21"],
                ];
             
            for block_list in D_MushPark_list:
                (byte_location, bit, name) = block_list
                byte = process_byte(byte_location)
                if byte[bit] != '1':
                    if name.endswith("1"):
                        location = "Blue Pi'illo Dreamworld"

                    else:
                        location = "Eldream Dream World"

                    collected_block_list.append([name, "D_MushPark", location])
                    total_blocks_collected -= 1
                    D_MushPark_number_collected -= 1

            #### Dreamy Dozing Sands ####
            D_DozSands_number_collected = 26

            D_DozSands_list = [
                    [0x0EB, 1, "D_DozSands_1"],
                    [0x0EB, 2, "D_DozSands_2"],
                    [0x0F0, 3, "D_DozSands_3"],
                    [0x0F1, 2, "D_DozSands_4"],
                    [0x0F1, 1, "D_DozSands_5"],
                    [0x0F1, 0, "D_DozSands_6"],
                    [0x0F2, 6, "D_DozSands_7"],
                    [0x0F0, 5, "D_DozSands_8"],
                    [0x0F4, 1, "D_DozSands_9"],
                    [0x0F8, 7, "D_DozSands_10"],
                    [0x0F8, 6, "D_DozSands_11"],
                    [0x0F9, 4, "D_DozSands_12"],
                    [0x0FA, 6, "D_DozSands_13"],
                    [0x0FC, 6, "D_DozSands_14"],
                    [0x0FC, 5, "D_DozSands_15"],
                    [0x0FF, 7, "D_DozSands_16"],
                    [0x0FF, 6, "D_DozSands_17"],
                    [0x100, 0, "D_DozSands_18"],
                    [0x101, 7, "D_DozSands_19"],
                    [0x101, 6, "D_DozSands_20"],
                    [0x100, 2, "D_DozSands_21"],
                    [0x100, 1, "D_DozSands_22"],
                    [0x100, 5, "D_DozSands_23"],
                    [0x100, 4, "D_DozSands_24"],
                    [0x100, 6, "D_DozSands_25"],
                    [0x100, 3, "D_DozSands_26"],
                ];
                          
            for block_list in D_DozSands_list:
                (byte_location, bit, name) = block_list
                byte = process_byte(byte_location)
                if byte[bit] != '1':
                    if any(name.endswith(f"{i}") for i in range(1, 3)):
                        location = "First Deco Pi'illo Dreamworld"
                    
                    if any(name.endswith(f"{i}") for i in range(3, 5)):
                        location = "Second Deco Pi'illo Dreamworld"

                    if any(name.endswith(f"{i}") for i in range(5, 7)):
                        location = "Third Deco Pi'illo Dreamworld"

                    if any(name.endswith(f"{i}") for i in range(7, 9)):
                        location = "Fourth Deco Pi'illo Dreamworld"
                        
                    if name.endswith("9"):
                        location = "Fifth Deco Pi'llo Dreamworld" 

                    if any(name.endswith(f"{i}") for i in range(10, 18)):
                        location = "Dream Stone Dreampoint"
                    
                    if name.endswith("18"):
                        location = "Pink Pi'illo 1 Dreamworld" 
    
                    if name.endswith("19"):
                        location = "Pink Pi'illo 3 Dreamworld" 

                    if any(name.endswith(f"{i}") for i in range(21, 23)):
                        location = "Pink Pi'illo 4 Dreamworld"

                    if any(name.endswith(f"{i}") for i in range(23, 27)):
                        location = "Dozing Mattress Dreamworld"

                    collected_block_list.append([name, "D_DozSands", location])
                    total_blocks_collected -= 1
                    D_DozSands_number_collected -= 1

            #### Dreamy Wakeport ####
            D_Wakeport_number_collected = 42
            D_Wakeport_list = [
                    [0x103, 0, "D_Wakeport_1"],
                    [0x104, 7, "D_Wakeport_2"],
                    [0x104, 6, "D_Wakeport_3"],
                    [0x104, 5, "D_Wakeport_4"],
                    [0x104, 4, "D_Wakeport_5"],
                    [0x104, 3, "D_Wakeport_6"],
                    [0x104, 2, "D_Wakeport_7"],
                    [0x167, 6, "D_Wakeport_8"],
                    [0x167, 5, "D_Wakeport_9"],
                    [0x106, 7, "D_Wakeport_10"],
                    [0x106, 6, "D_Wakeport_11"],
                    [0x106, 4, "D_Wakeport_12"],
                    [0x106, 5, "D_Wakeport_13"],
                    [0x105, 7, "D_Wakeport_14"],
                    [0x104, 0, "D_Wakeport_15"],
                    [0x104, 1, "D_Wakeport_16"],
                    [0x105, 6, "D_Wakeport_17"],
                    [0x105, 5, "D_Wakeport_18"],
                    [0x105, 4, "D_Wakeport_19"],
                    [0x105, 3, "D_Wakeport_20"],
                    [0x105, 2, "D_Wakeport_21"],
                    [0x105, 1, "D_Wakeport_22"],
                    [0x105, 0, "D_Wakeport_23"],
                    [0x106, 3, "D_Wakeport_24"],
                    [0x106, 2, "D_Wakeport_25"],
                    [0x117, 6, "D_Wakeport_26"],
                    [0x117, 7, "D_Wakeport_27"],
                    [0x117, 3, "D_Wakeport_28"],
                    [0x106, 1, "D_Wakeport_29"],
                    [0x10F, 6, "D_Wakeport_30"],
                    [0x10F, 2, "D_Wakeport_31"],
                    [0x10F, 3, "D_Wakeport_32"],
                    [0x116, 1, "D_Wakeport_33"],
                    [0x116, 0, "D_Wakeport_34"],
                    [0x112, 1, "D_Wakeport_35"],
                    [0x112, 0, "D_Wakeport_36"],
                    [0x113, 7, "D_Wakeport_37"],
                    [0x116, 4, "D_Wakeport_38"],
                    [0x116, 3, "D_Wakeport_39"],
                    [0x116, 5, "D_Wakeport_40"],
                    [0x116, 2, "D_Wakeport_41"],
                    [0x117, 2, "D_Wakeport_42"],
                ];
        
            for block_list in D_Wakeport_list:
                (byte_location, bit, name) = block_list
                byte = process_byte(byte_location)
                if byte[bit] != '1':
                    if any(name.endswith(f"{i}") for i in range(1, 26)):
                        location = "Big Massif Dreampoint"
                    
                    if any(name.endswith(f"{i}") for i in range(26, 28)):
                        location = "Pink Pi'illo 1 Dreampoint"

                    if name.endswith("28"):
                        location = "Pink Pi'illo 3 Dreampoint"

                    if any(name.endswith(f"{i}") for i in range(29, 42)):
                        location = "Bedsmith Dreampoint"
                    
                    if name.endswith("42"):
                        location = "Pink Pi'illo 5 Dreampoint"

                    collected_block_list.append([name, "D_Wakeport", location])
                    total_blocks_collected -= 1
                    D_Wakeport_number_collected -= 1
                
            #### Dreamy Mount Pajamaja ####
            D_MountPaj_number_collected = 61

            D_MountPaj_list = [
                    [0x125, 0, "D_MountPaj_1"],
                    [0x126, 7, "D_MountPaj_2"],
                    [0x12A, 3, "D_MountPaj_3"],
                    [0x12A, 5, "D_MountPaj_4"],
                    [0x12A, 4, "D_MountPaj_5"],
                    [0x12A, 7, "D_MountPaj_6"],
                    [0x12A, 6, "D_MountPaj_7"],
                    [0x12A, 2, "D_MountPaj_8"],
                    [0x12A, 1, "D_MountPaj_9"],
                    [0x196, 1, "D_MountPaj_10"],
                    [0x193, 3, "D_MountPaj_11"],
                    [0x12A, 0, "D_MountPaj_12"],
                    [0x12B, 7, "D_MountPaj_13"],
                    [0x12B, 6, "D_MountPaj_14"],
                    [0x12B, 5, "D_MountPaj_15"],
                    [0x12B, 2, "D_MountPaj_16"],
                    [0x12B, 1, "D_MountPaj_17"],
                    [0x12B, 4, "D_MountPaj_18"],
                    [0x12B, 3, "D_MountPaj_19"],
                    [0x12C, 6, "D_MountPaj_20"],
                    [0x12B, 0, "D_MountPaj_21"],
                    [0x12C, 7, "D_MountPaj_22"],
                    [0x12C, 3, "D_MountPaj_23"],
                    [0x12C, 2, "D_MountPaj_24"],
                    [0x12C, 5, "D_MountPaj_25"],
                    [0x12C, 4, "D_MountPaj_26"],
                    [0x199, 1, "D_MountPaj_27"],
                    [0x199, 0, "D_MountPaj_28"],
                    [0x12D, 5, "D_MountPaj_29"],
                    [0x12D, 7, "D_MountPaj_30"],
                    [0x12D, 6, "D_MountPaj_31"],
                    [0x12D, 4, "D_MountPaj_32"],
                    [0x12D, 3, "D_MountPaj_33"],
                    [0x12D, 2, "D_MountPaj_34"],
                    [0x12D, 1, "D_MountPaj_35"],
                    [0x12E, 7, "D_MountPaj_36"],
                    [0x12D, 0, "D_MountPaj_37"],
                    [0x12F, 6, "D_MountPaj_38"],
                    [0x12F, 5, "D_MountPaj_39"],
                    [0x130, 6, "D_MountPaj_40"],
                    [0x130, 5, "D_MountPaj_41"],
                    [0x130, 0, "D_MountPaj_42"],
                    [0x131, 7, "D_MountPaj_43"],
                    [0x1E3, 2, "D_MountPaj_44"],
                    [0x130, 2, "D_MountPaj_45"],
                    [0x130, 1, "D_MountPaj_46"],
                    [0x131, 5, "D_MountPaj_47"],
                    [0x131, 4, "D_MountPaj_48"],
                    [0x131, 3, "D_MountPaj_49"],
                    [0x132, 6, "D_MountPaj_50"],
                    [0x132, 7, "D_MountPaj_51"],
                    [0x133, 7, "D_MountPaj_52"],
                    [0x133, 6, "D_MountPaj_53"],
                    [0x1A7, 4, "D_MountPaj_54"],
                    [0x13B, 4, "D_MountPaj_55"],
                    [0x13B, 5, "D_MountPaj_56"],
                    [0x133, 0, "D_MountPaj_57"],
                    [0x134, 7, "D_MountPaj_58"],
                    [0x133, 1, "D_MountPaj_59"],
                    [0x133, 2, "D_MountPaj_60"],
                    [0x133, 5, "D_MountPaj_61"],
                ];
 
            for block_list in D_MountPaj_list:
                (byte_location, bit, name) = block_list
                byte = process_byte(byte_location)
                if byte[bit] != '1':
                    if any(name.endswith(f"{i}") for i in range(1, 3)):
                        location = "Mega Phil Dreamworld"
                    
                    if any(name.endswith(f"{i}") for i in range(3, 8)):
                        location = "Mega Lowe Dreamworld"

                    if any(name.endswith(f"{i}") for i in range(8, 10)):
                        location = "Mega Cush Dreamworld"

                    if any(name.endswith(f"{i}") for i in range(10, 12)):
                        location = "Mega Shawn Dreamworld"

                    if any(name.endswith(f"{i}") for i in range(12, 55)):
                        location = "Peak Dreampoint"

                    if any(name.endswith(f"{i}") for i in range(55, 57)):
                        location = "Pink Pi'illo 2 Dreamworld"

                    if any(name.endswith(f"{i}") for i in range(57, 60)):
                        location = "Pink Pi'illo 4 Dreamworld"

                    if any(name.endswith(f"{i}") for i in range(60, 62)):
                        location = "Pajamaja Rock Frame Dreampoint"
                    
                    collected_block_list.append([name, "D_MountPaj", location])
                    total_blocks_collected -= 1
                    D_MountPaj_number_collected -= 1

            #### Dreamy Driftwood Shore ####
            D_DriftShore_number_collected = 30
             
            D_DriftShore_list = [
                    [0x153, 4, "D_DriftShore_1"],
                    [0x154, 5, "D_DriftShore_2"],
                    [0x154, 4, "D_DriftShore_3"],
                    [0x154, 3, "D_DriftShore_4"],
                    [0x158, 2, "D_DriftShore_5"],
                    [0x155, 4, "D_DriftShore_6"],
                    [0x15A, 7, "D_DriftShore_7"],
                    [0x15A, 5, "D_DriftShore_8"],
                    [0x156, 1, "D_DriftShore_9"],
                    [0x156, 2, "D_DriftShore_10"],
                    [0x15B, 5, "D_DriftShore_11"],
                    [0x143, 1, "D_DriftShore_12"],
                    [0x143, 0, "D_DriftShore_13"],
                    [0x157, 3, "D_DriftShore_14"],
                    [0x157, 2, "D_DriftShore_15"],
                    [0x157, 4, "D_DriftShore_16"],
                    [0x15A, 6, "D_DriftShore_17"],
                    [0x14B, 1, "D_DriftShore_18"],
                    [0x158, 3, "D_DriftShore_19"],
                    [0x15F, 3, "D_DriftShore_20"],
                    [0x15F, 4, "D_DriftShore_21"],
                    [0x15F, 1, "D_DriftShore_22"],
                    [0x165, 5, "D_DriftShore_23"],
                    [0x165, 4, "D_DriftShore_24"],
                    [0x165, 3, "D_DriftShore_25"],
                    [0x165, 2, "D_DriftShore_26"],
                    [0x166, 4, "D_DriftShore_27"],
                    [0x166, 3, "D_DriftShore_28"],
                    [0x165, 7, "D_DriftShore_29"],
                    [0x165, 6, "D_DriftShore_30"],
                ];

            for block_list in D_DriftShore_list:
                (byte_location, bit, name) = block_list
                byte = process_byte(byte_location)
                if byte[bit] != '1':
                    if any(name.endswith(f"{i}") for i in range(1, 20)):
                        location = "Seadric's Dreampoint"
                    
                    if any(name.endswith(f"{i}") for i in range(20, 23)):
                        location = "Seabury's Dreamworld"

                    if any(name.endswith(f"{i}") for i in range(23, 28)):
                        location = "Pink Pi'illo 1 Dreamworld"

                    if name.endswith("28"):
                        location = "Pink Pi'illo 2 Dreamworld"

                    if any(name.endswith(f"{i}") for i in range(29, 31)):
                        location = "Pink Pi'illo 3 Dreamworld"

                    collected_block_list.append([name, "D_DriftShore", location])
                    total_blocks_collected -= 1
                    D_DriftShore_number_collected -= 1

            #### Dreamy Somnom Woods ####
            D_SomWoods_number_collected = 51

            D_SomWoods_list = [
                    [0x1AE, 7, "D_SomWoods_1"],
                    [0x1AE, 6, "D_SomWoods_2"],
                    [0x1AE, 5, "D_SomWoods_3"],
                    [0x1AE, 2, "D_SomWoods_4"],
                    [0x1AE, 4, "D_SomWoods_5"],
                    [0x1AE, 3, "D_SomWoods_6"],
                    [0x1AE, 1, "D_SomWoods_7"],
                    [0x1B3, 5, "D_SomWoods_8"],
                    [0x1B3, 6, "D_SomWoods_9"],
                    [0x1B3, 7, "D_SomWoods_10"],
                    [0x1B4, 7, "D_SomWoods_11"],
                    [0x1B4, 6, "D_SomWoods_12"],
                    [0x1B4, 4, "D_SomWoods_13"],
                    [0x1B4, 5, "D_SomWoods_14"],
                    [0x1B4, 3, "D_SomWoods_15"],
                    [0x1B4, 2, "D_SomWoods_16"],
                    [0x1B4, 1, "D_SomWoods_17"],
                    [0x1B4, 0, "D_SomWoods_18"],
                    [0x1B5, 2, "D_SomWoods_19"],
                    [0x1B5, 7, "D_SomWoods_20"],
                    [0x1B5, 6, "D_SomWoods_21"],
                    [0x1B5, 5, "D_SomWoods_22"],
                    [0x1B5, 4, "D_SomWoods_23"],
                    [0x1B5, 3, "D_SomWoods_24"],
                    [0x1B5, 0, "D_SomWoods_25"],
                    [0x1B8, 2, "D_SomWoods_26"],
                    [0x22E, 5, "D_SomWoods_27"],
                    [0x1B5, 1, "D_SomWoods_28"],
                    [0x1B6, 4, "D_SomWoods_29"],
                    [0x1B8, 3, "D_SomWoods_30"],
                    [0x1B8, 4, "D_SomWoods_31"],
                    [0x1B8, 1, "D_SomWoods_32"],
                    [0x1B9, 4, "D_SomWoods_33"],
                    [0x1B9, 0, "D_SomWoods_34"],
                    [0x1BA, 5, "D_SomWoods_35"],
                    [0x1BA, 4, "D_SomWoods_36"],
                    [0x1B9, 1, "D_SomWoods_37"],
                    [0x1B9, 5, "D_SomWoods_38"],
                    [0x1B9, 3, "D_SomWoods_39"],
                    [0x1B9, 2, "D_SomWoods_40"],
                    [0x1DE, 4, "D_SomWoods_41"],
                    [0x1BC, 6, "D_SomWoods_42"],
                    [0x1DB, 0, "D_SomWoods_43"],
                    [0x1DC, 7, "D_SomWoods_44"],
                    [0x1BC, 2, "D_SomWoods_45"],
                    [0x1BC, 1, "D_SomWoods_46"],
                    [0x1BC, 0, "D_SomWoods_47"],
                    [0x1BD, 7, "D_SomWoods_48"],
                    [0x1BD, 6, "D_SomWoods_49"],
                    [0x1BD, 5, "D_SomWoods_50"],
                    [0x1BD, 4, "D_SomWoods_51"],
                ];
             
            for block_list in D_SomWoods_list:
                (byte_location, bit, name) = block_list
                byte = process_byte(byte_location)
                if byte[bit] != '1':
                    if any(name.endswith(f"{i}") for i in range(1, 3)):
                        location = "Pi'illo Master 1 Dreamworld"
                    
                    if any(name.endswith(f"{i}") for i in range(3, 8)):
                        location = "Pi'illo Master 2 Dreamworld"

                    if any(name.endswith(f"{i}") for i in range(8, 10)):
                        location = "Pi'illo Master 3 Dreamworld"

                    if name.endswith(f"10"):
                        location = "Pi'illo Master 4 Dreamworld"

                    if any(name.endswith(f"{i}") for i in range(11, 15)):
                        location = "Pi'illo Master 5 Dreamworld"

                    if any(name.endswith(f"{i}") for i in range(15, 43)):
                        location = "Zeekeeper Dreampoint"

                    if any(name.endswith(f"{i}") for i in range(43, 45)):
                        location = "Pink Pi'illo 1 Dreamworld"
                    
                    if any(name.endswith(f"{i}") for i in range(45, 48)):
                        location = "Pink Pi'illo 2 Dreamworld'"

                    if name.endswith("48"):
                        location = "Pink Pi'illo 3 Dreamworld"
                    
                    if any(name.endswith(f"{i}") for i in range(49, 51)):
                        location = "Pink Pi'illo 4 Dreamworld'"

                    if name.endswith("51"):
                        location = "Pink Pi'illo 5 Dreamworld"

                    collected_block_list.append([name, "D_SomWoods", location])
                    total_blocks_collected -= 1
                    D_SomWoods_number_collected -= 1

            #### Dreamy Neo Bowser Castle ####
            D_NBC_number_collected = 43
            
            D_NBC_list = [
                    [0x1C3, 0, "D_NBC_1"],
                    [0x1C3, 1, "D_NBC_2"],
                    [0x1C3, 2, "D_NBC_3"],
                    [0x1C4, 7, "D_NBC_4"],
                    [0x1C4, 6, "D_NBC_5"],
                    [0x1C4, 5, "D_NBC_6"],
                    [0x1C4, 4, "D_NBC_7"],
                    [0x1CB, 4, "D_NBC_8"],
                    [0x1CB, 3, "D_NBC_9"],
                    [0x1CB, 2, "D_NBC_10"],
                    [0x1CB, 1, "D_NBC_11"],
                    [0x1CC, 7, "D_NBC_12"],
                    [0x1CB, 0, "D_NBC_13"],
                    [0x1C3, 4, "D_NBC_14"],
                    [0x1CC, 6, "D_NBC_15"],
                    [0x1CC, 5, "D_NBC_16"],
                    [0x1C3, 5, "D_NBC_17"],
                    [0x1C3, 3, "D_NBC_18"],
                    [0x1CC, 4, "D_NBC_19"],
                    [0x1DE, 3, "D_NBC_20"],
                    [0x1CC, 3, "D_NBC_21"],
                    [0x1CC, 0, "D_NBC_22"],
                    [0x1CD, 7, "D_NBC_23"],
                    [0x1CD, 6, "D_NBC_24"],
                    [0x1CD, 5, "D_NBC_25"],
                    [0x1DE, 2, "D_NBC_26"],
                    [0x1CD, 3, "D_NBC_27"],
                    [0x1CE, 1, "D_NBC_28"],
                    [0x1CF, 7, "D_NBC_29"],
                    [0x1CE, 0, "D_NBC_30"],
                    [0x1CF, 0, "D_NBC_31"],
                    [0x1D0, 1, "D_NBC_32"],
                    [0x1D0, 2, "D_NBC_33"],
                    [0x1D0, 0, "D_NBC_34"],
                    [0x1D4, 6, "D_NBC_35"],
                    [0x1D4, 5, "D_NBC_36"],
                    [0x1D4, 4, "D_NBC_37"],
                    [0x1D4, 3, "D_NBC_38"],
                    [0x1D4, 2, "D_NBC_39"],
                    [0x1E1, 1, "D_NBC_40"],
                    [0x1D6, 2, "D_NBC_41"],
                    [0x1D6, 1, "D_NBC_42"],
                    [0x1D6, 0, "D_NBC_43"],
                ];
             
            for block_list in D_NBC_list:
                (byte_location, bit, name) = block_list
                byte = process_byte(byte_location)
                if byte[bit] != '1':
                    if any(name.endswith(f"{i}") for i in range(1, 20)):
                        location = "Koopa Clown Car Dreampoint 1"
                    
                    if any(name.endswith(f"{i}") for i in range(20, 24)):
                        location = "Koopa Clown Car Dreampoint 2"

                    if any(name.endswith(f"{i}") for i in range(24, 29)):
                        location = "Koopa Clown Car Dreampoint 3"

                    if any(name.endswith(f"{i}") for i in range(29, 31)):
                        location = "Koopa Clown Car Dreampoint 4"

                    if name.endswith("31"):
                        location = "Dark Stone Platform Dreampoint 1"


                    if any(name.endswith(f"{i}") for i in range(32, 35)):
                        location = "Dark Stone Platform Dreampoint 2"

                    if any(name.endswith(f"{i}") for i in range(35, 44)):
                        location = "Bowser Dreampoint"
                    
                    collected_block_list.append([name, "D_NBC", location])
                    total_blocks_collected -= 1
                    D_NBC_number_collected -= 1


            stats_list = [
                total_blocks_collected, PilloBlimp_number_collected, 
                PilloCastle_number_collected, D_PilloCastle_number_collected,
                MushPark_number_collected, D_MushPark_number_collected, 
                DozSands_number_collected, D_DozSands_number_collected, 
                Wakeport_number_collected, D_Wakeport_number_collected, 
                MountPaj_number_collected, D_MountPaj_number_collected, 
                DriftShore_number_collected, D_DriftShore_number_collected, 
                SomWoods_number_collected, D_SomWoods_number_collected, 
                NBC_number_collected, D_NBC_number_collected
            ];

            self.table = Table(collected_block_list, stats_list)
            self.table.show()

            # Close the current GUI
            self.close()


            
       
class Table(QWidget):
    def __init__(self, collected_block_list, stats_list):

        collected_block_rows = 0
        for i in collected_block_list:
            collected_block_rows += 1
        
        # Creates table layout, two spreadsheets horizontally
        super().__init__()
        self.setWindowTitle("Block-Recovery Rate Helper")
        self.setGeometry(100, 100, 2400, 1600)
        self.layout = QHBoxLayout()
        self.left_table = QTableWidget()
        self.right_table = QTableWidget()
        #########

        #Creating and formatting the left and right tables
        self.layout.addWidget(self.left_table)
        self.layout.addWidget(self.right_table)

        self.left_table.setRowCount(collected_block_rows)
        self.left_table.setColumnCount(3)

        self.right_table.setRowCount(11)
        self.right_table.setColumnCount(2)
        #########

        # Left Table
        self.left_table.setHorizontalHeaderLabels(["Name", "Location", "Image"])

        self.left_table.setColumnWidth(0, 250)
        self.left_table.setColumnWidth(1, 250)
        self.left_table.setColumnWidth(2, 760)

        self.populate_left_table(collected_block_list)
        #########

        # Right Table
        self.right_table.setHorizontalHeaderLabels(["Block-Recovery", "Rate Statistics"])
        self.right_table.setColumnWidth(0, 500)
        self.right_table.setColumnWidth(1, 500)

        for i in range(0, 10):
            self.right_table.setRowHeight(i, 100) 
        
        self.right_table.setRowHeight(10, 300)

        self.populate_right_table(stats_list)
        ######

        self.setLayout(self.layout)

    def populate_left_table(self, collected_block_list):
        current_row = 0
        for block in collected_block_list:
            (name, program_identifier, location) = block

            self.left_table.setRowHeight(current_row, 320)
            self.left_table.setItem(current_row, 0, QTableWidgetItem(name))
            self.left_table.setItem(current_row, 1, QTableWidgetItem(location))

            ######## Image shenanigans
            # Get image
            current_directory = os.getcwd()
            image_path = os.path.join(current_directory, "Pictures/", program_identifier, name)
            pixmap = QPixmap(image_path)

            # Resize image
            label = QLabel()
            label.setPixmap(pixmap.scaled(720, 240, aspectRatioMode=1))  # Resize the image to fit
            label.setFixedSize(720, 240)  # Set a fixed size for the label
            label.setScaledContents(True)  # Scale the image to fit the label

            # Centers image vertically within its cell
            hbox = QHBoxLayout()
            hbox.addWidget(label)
            vbox = QVBoxLayout()
            vbox.addStretch()  
            vbox.addLayout(hbox)  
            vbox.addStretch()
            image_widget = QWidget()
            image_widget.setLayout(vbox)

            self.left_table.setCellWidget(current_row, 2, image_widget) 
            ########

            current_row += 1

    def populate_right_table(self, stats_list):
        
        self.right_table.setItem(0, 0, QTableWidgetItem(f"Pi'illo Blimport: {stats_list[1]}/12"))
        self.right_table.setItem(0, 1, QTableWidgetItem(f"Total Blocks Collected: {stats_list[0]}/681"))

        self.right_table.setItem(1, 0, QTableWidgetItem(f"Pi'illo Castle: {stats_list[2]}/30"))
        self.right_table.setItem(1, 1, QTableWidgetItem(f"Dreamy Pi'illo Castle: {stats_list[3]}/52"))

        self.right_table.setItem(2, 0, QTableWidgetItem(f"Mushrise Park: {stats_list[4]}/50"))
        self.right_table.setItem(2, 1, QTableWidgetItem(f"Dreamy Mushrise Park: {stats_list[5]}/21"))

        self.right_table.setItem(3, 0, QTableWidgetItem(f"Dozing Sands: {stats_list[6]}/61"))
        self.right_table.setItem(3, 1, QTableWidgetItem(f"Dreamy Dozing Sands: {stats_list[7]}/26"))

        self.right_table.setItem(4, 0, QTableWidgetItem(f"Wakeport: {stats_list[8]}/33"))
        self.right_table.setItem(4, 1, QTableWidgetItem(f"Dreamy Wakeport: {stats_list[9]}/42"))

        self.right_table.setItem(5, 0, QTableWidgetItem(f"Mount Pajamaja: {stats_list[10]}/47"))
        self.right_table.setItem(5, 1, QTableWidgetItem(f"Dreamy Mount Pajamaja: {stats_list[11]}/61"))

        self.right_table.setItem(6, 0, QTableWidgetItem(f"Driftwood Shores: {stats_list[12]}/30"))
        self.right_table.setItem(6, 1, QTableWidgetItem(f"Dreamy Driftwood Shores: {stats_list[13]}/30"))

        self.right_table.setItem(7, 0, QTableWidgetItem(f"Somnom Woods: {stats_list[14]}/33"))
        self.right_table.setItem(7, 1, QTableWidgetItem(f"Dreamy Somnom Woods: {stats_list[15]}/51"))

        self.right_table.setItem(8, 0, QTableWidgetItem(f"Neo Bowser Castle: {stats_list[16]}/59"))
        self.right_table.setItem(8, 1, QTableWidgetItem(f"Dreamy Neo Bowser Castle: {stats_list[17]}/43"))\

        BRR = round((stats_list[0] / 681) * 100, 2)

        self.right_table.setItem(9, 0, QTableWidgetItem(f"Block-Recovery Rate: {BRR}%"))
    
        if stats_list[0] == 681:
            self.right_table.setItem(9, 1, QTableWidgetItem(f"Congratulations! You've collected every block!"))
        else:
            left_to_go = 681 - stats_list[0]
            self.right_table.setItem(9, 1, QTableWidgetItem(f"{left_to_go} left to go!"))

        self.right_table.setItem(10, 1, QTableWidgetItem(f"Credit to the Super Mario Wiki for images: https://www.mariowiki.com/List_of_real_world_blocks_in_Mario_%26_Luigi:_Dream_Team, https://www.mariowiki.com/List_of_Dream_World_blocks_in_Mario_%26_Luigi:_Dream_Team"))

        self.right_table.setItem(10, 0, QTableWidgetItem(f"Need more context for Pi'illo Dreamworld locations? Check here: https://www.mariowiki.com/Pi%27illo"))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainGUI()
    window.show()
    sys.exit(app.exec_())
