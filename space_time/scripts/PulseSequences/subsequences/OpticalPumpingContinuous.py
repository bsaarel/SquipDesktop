from common.okfpgaservers.pulser.pulse_sequences.pulse_sequence import pulse_sequence

from labrad.units import WithUnit

class optical_pumping_continuous(pulse_sequence):
    
    
    required_parameters = [
                  ('OpticalPumpingContinuous','optical_pumping_continuous_duration'),
                  ('OpticalPumpingContinuous','optical_pumping_continuous_repump_additional'),
                  ('OpticalPumpingContinuous','optical_pumping_continuous_frequency_854'),
                  ('OpticalPumpingContinuous','optical_pumping_continuous_amplitude_854'),
                  ('OpticalPumpingContinuous','optical_pumping_continuous_frequency_729'),
                  ('OpticalPumpingContinuous','optical_pumping_continuous_amplitude_729'),
                  ('OpticalPumpingContinuous','optical_pumping_continuous_frequency_866'), 
                  ('OpticalPumpingContinuous','optical_pumping_continuous_amplitude_866'),
                  
                  ('OpticalPumpingAux','aux_op_enable'),
                  ('OpticalPumpingAux','aux_optical_pumping_amplitude_729'),
                  ('OpticalPumpingAux','aux_optical_frequency_729'),
                  
                  ('StatePreparation', 'channel_729')
                  ]

    def sequence(self):
        gap_time = WithUnit(1.0, 'us')
        
        opc = self.parameters.OpticalPumpingContinuous
        channel_729 = self.parameters.StatePreparation.channel_729
        
        #repump_dur_854 = opc.optical_pumping_continuous_duration + opc.optical_pumping_continuous_repump_additional
        #repump_dur_866 = opc.optical_pumping_continuous_duration + 2 * opc.optical_pumping_continuous_repump_additional
        #
        #self.end = self.start + repump_dur_866
        #
        #self.addDDS(channel_729, self.start, opc.optical_pumping_continuous_duration, opc.optical_pumping_continuous_frequency_729, opc.optical_pumping_continuous_amplitude_729)
        ##print 'op:', opc.optical_pumping_continuous_frequency_729
        #self.addDDS('854', self.start, repump_dur_854, opc.optical_pumping_continuous_frequency_854, opc.optical_pumping_continuous_amplitude_854)
        #self.addDDS('866', self.start, repump_dur_866, opc.optical_pumping_continuous_frequency_866, opc.optical_pumping_continuous_amplitude_866)

        repump_dur_854 = opc.optical_pumping_continuous_repump_additional
        repump_dur_866 = 2 * opc.optical_pumping_continuous_repump_additional
        
        self.end = self.start + opc.optical_pumping_continuous_duration + repump_dur_866 + gap_time
        
        self.addDDS(channel_729, self.start, opc.optical_pumping_continuous_duration, opc.optical_pumping_continuous_frequency_729, opc.optical_pumping_continuous_amplitude_729)
        #print 'op:', opc.optical_pumping_continuous_frequency_729
        self.addDDS('854', self.start, opc.optical_pumping_continuous_duration, opc.optical_pumping_continuous_frequency_854, opc.optical_pumping_continuous_amplitude_854)
        self.addDDS('866', self.start, opc.optical_pumping_continuous_duration, opc.optical_pumping_continuous_frequency_866, opc.optical_pumping_continuous_amplitude_866)

        repump_854_power = WithUnit(-10.0, 'dBm')
        repump_866_power = WithUnit(-10.0, 'dBm')

        self.addDDS('854', self.start + opc.optical_pumping_continuous_duration + gap_time, repump_dur_854, opc.optical_pumping_continuous_frequency_854, repump_854_power)
        self.addDDS('866', self.start + opc.optical_pumping_continuous_duration + gap_time, repump_dur_866, opc.optical_pumping_continuous_frequency_866, repump_866_power)


        aux = self.parameters.OpticalPumpingAux
        if aux.aux_op_enable:
            self.addDDS('729DP_aux', self.start, opc.optical_pumping_continuous_duration, aux.aux_optical_frequency_729, aux.aux_optical_pumping_amplitude_729)
            #print 'aux op:', aux.aux_optical_frequency_729
# class optical_pumping_continuous(pulse_sequence):
#     
#     
#     required_parameters = [
#                   ('OpticalPumpingContinuous','optical_pumping_continuous_duration'),
#                   ('OpticalPumpingContinuous','optical_pumping_continuous_repump_additional'),
#                   ('OpticalPumpingContinuous','optical_pumping_continuous_frequency_854'),
#                   ('OpticalPumpingContinuous','optical_pumping_continuous_amplitude_854'),
#                   ('OpticalPumpingContinuous','optical_pumping_continuous_frequency_729'),
#                   ('OpticalPumpingContinuous','optical_pumping_continuous_amplitude_729'),
#                   ('OpticalPumpingContinuous','optical_pumping_continuous_frequency_866'), 
#                   ('OpticalPumpingContinuous','optical_pumping_continuous_amplitude_866'),
#             
#                   ]
# 
#     def sequence(self):
#         opc = self.parameters.OpticalPumpingContinuous
#         repump_dur_854 = opc.optical_pumping_continuous_duration + opc.optical_pumping_continuous_repump_additional
#         repump_dur_866 = opc.optical_pumping_continuous_duration + 2 * opc.optical_pumping_continuous_repump_additional
#         self.end = self.start + repump_dur_866
#         self.addDDS('729', self.start, opc.optical_pumping_continuous_duration, opc.optical_pumping_continuous_frequency_729, opc.optical_pumping_continuous_amplitude_729)
#         self.addDDS('854', self.start, repump_dur_854, opc.optical_pumping_continuous_frequency_854, opc.optical_pumping_continuous_amplitude_854)
#         self.addDDS('866', self.start, repump_dur_866, opc.optical_pumping_continuous_frequency_866, opc.optical_pumping_continuous_amplitude_866)
