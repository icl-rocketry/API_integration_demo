#Author-DEEEV
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        ui.messageBox('Hello script')

        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        if not design:
            ui.messageBox('No active Fusion design', title)
            return

        # Get the root component of the active design
        rootComp = design.rootComponent

        # Get physical properties from component (high accuracy)
        physicalProperties = rootComp.getPhysicalProperties(adsk.fusion.CalculationAccuracy.HighCalculationAccuracy)

        mass = physicalProperties.mass
        cog = physicalProperties.centerOfMass.getData()
        mom_of_i = physicalProperties.getXYZMomentsOfInertia()

        ui.messageBox(f'Mass (kg): {mass}')
        if cog[0]:
            ui.messageBox(f'Center of Gravity (m?): \n x = {cog[1]}\n y = {cog[2]}\n z = {cog[3]}')
        else:
            ui.messageBox("Center of gravity extraction failed!")

        if mom_of_i[0]:
            ui.messageBox(f'Moments of Inertia (kg/cm^2): \n xx: {mom_of_i[1]} \n yy: {mom_of_i[2]} \n zz: {mom_of_i[3]} \n xy: {mom_of_i[4]} \n yz: {mom_of_i[5]} \n xz: {mom_of_i[6]}')
        else:
            ui.messageBox('Moment of Inertia extraction failed!')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
