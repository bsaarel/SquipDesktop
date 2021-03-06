from common.okfpgaservers.pulser.pulse_sequences.pulse_sequence import pulse_sequence
from subsequences.RepumpDwithDoppler import doppler_cooling_after_repump_d
from subsequences.EmptySequence import empty_sequence
from subsequences.OpticalPumping import optical_pumping
from subsequences.RabiExcitation import rabi_excitation_with_sigma
from subsequences.Tomography import tomography_readout
from subsequences.TurnOffAll import turn_off_all
from subsequences.SidebandCooling import sideband_cooling
from subsequences.EitCooling import eit_cooling
from subsequences.motion_analysis import motion_analysis
from subsequences.pi_rotation import pi_rotation
from labrad.units import WithUnit
from treedict import TreeDict

class spectrum_rabi_after_pi(pulse_sequence):
    
    required_parameters = [ 
                           ('Heating', 'background_heating_time'),
                           ('StatePreparation','optical_pumping_enable'), 
                           ('StatePreparation','sideband_cooling_enable'),
                           ('StatePreparation','eit_cooling_enable'),
                           ('Motion_Analysis','excitation_enable'),
                           ('RabiFlopping','rabi_amplitude_729')
                           ]
    
    required_subsequences = [doppler_cooling_after_repump_d, empty_sequence, optical_pumping, 
                             rabi_excitation_with_sigma, tomography_readout, turn_off_all, sideband_cooling,
                             eit_cooling,pi_rotation]
    
    replaced_parameters = {empty_sequence:[('EmptySequence','empty_sequence_duration'),],pi_rotation:[('PiRotation','pi_rotation_amplitude'),]}

    def sequence(self):
        p = self.parameters
        self.end = WithUnit(10, 'us')
        self.addSequence(turn_off_all)
        
        self.addSequence(doppler_cooling_after_repump_d)
        if p.StatePreparation.optical_pumping_enable:
            self.addSequence(optical_pumping)
        if p.StatePreparation.eit_cooling_enable:
            self.addSequence(eit_cooling)
        if p.StatePreparation.sideband_cooling_enable:
            self.addSequence(sideband_cooling)
        
        self.addSequence(pi_rotation,TreeDict.fromdict({'PiRotation.pi_rotation_amplitude':p.RabiFlopping.rabi_amplitude_729}))
                    
        self.addSequence(empty_sequence, TreeDict.fromdict({'EmptySequence.empty_sequence_duration':p.Heating.background_heating_time}))
        
        self.addSequence(rabi_excitation_with_sigma)
        self.addSequence(tomography_readout)
