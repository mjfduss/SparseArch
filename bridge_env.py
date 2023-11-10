from collections.abc import Sequence
from enum import Enum

CABLE_ANCHORAGE_X_OFFSET = 32

class Joint():
    def __init__(self, number: int, x: int, y: int):
        self.number = number
        self.x = x
        self.y = y

class CrossSection():
    def __init__(self, material: int, section: int, size: int):
        self.material = material
        self.section = section
        self.size = size

class Member():
    def __init__(self, 
        number: int, 
        start_joint: type[Joint], 
        end_joint: type[Joint], 
        x_section: type[CrossSection], 
        compression: str,
        tension: str):
        self.number = number
        self.start_joint = start_joint 
        self.end_joint = end_joint 
        self.x_section = x_section
        self.compression = compression
        self.tension = tension

class SupportTypes(Enum):
    ARCH_SUPPORT = 1
    CABLE_SUPPORT_LEFT = 2
    CABLE_SUPPORT_RIGHT = 4
    INTERMEDIATE_SUPPORT = 8
    HI_NOT_LO = 16

class ScenarioDescriptor():
    def __init__(self, index: int, id: str, number: int, site_cost: float):
        self.index = index
        self.id = id
        self.number = number
        self.site_cost = site_cost
        
class LoadScenario():
    """
    def __init__(self, 
        
        grid_size: float, 
        joint_radius: float, 
        load_case: str, 
        n_panels: int, 
        num_length_grids: int, 
        over_meters: int, 
        under_meters: int, 
        under_grids: int, 
        support_type: int, 
        intermediate_support_joint_no: int,
        n_loaded_joints: int,
        n_prescribed_joints: int,
        prescribed_joints: Sequence[Joint]
       ):
        """
    def __init__(self, desc: type[ScenarioDescriptor]):

        # ===================
        # Setup Support Types
        # ===================

        self.support_type = 0
        # digit 10 => (0 = low pier, 1 = high pier)
        if (desc.id[9] > '0'):
            self.support_type = SupportTypes.HI_NOT_LO
        
        # digit 9 => panel point at which pier is located. (0 = no pier).
        self.intermediate_support_joint_no = int(desc.id[8])
        if (self.intermediate_support_joint_no > 0):
            self.support_type = SupportTypes.INTERMEDIATE_SUPPORT
        """
        self.grid_size = grid_size
        self.joint_radius = joint_radius 
        self.load_case = load_case
        self.n_panels = n_panels
        self.num_length_grids = num_length_grids
        self.over_meters = over_meters
        self.under_meters = under_meters
        self.under_grids = under_grids
        
        self.intermediate_support_joint_no = intermediate_support_joint_no
        self.n_loaded_joints = n_loaded_joints
        self.n_prescribed_joints = n_prescribed_joints
        self.prescribed_joints = prescribed_joints
        """


class BridgeError(Enum):
    BridgeNoError = 1
    BridgeTooManyElements = 2
    BridgeTooFewJoints = 3
    BridgeWrongPrescribedJoints = 4
    BridgeTooFewMembers = 5
    BridgeDupJoints = 6
    BridgeDupMembers = 7
    BridgeJointOnMember = 8

class Bridge():
    def __init__(self, load_scenario: type[LoadScenario]):
        self.error = BridgeError.BridgeNoError

    
