#Author-DEEEV
#Description-


from .Modules import valispace
import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):

    # create the valispace env



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


        vali_url = 'https://iclrocketry.valispace.com'
        username = 'devansh.agrawal16'
        password = 'valie6ipi=-1'
        ui.messageBox(f'{vali_url}')
        try:
            vs = valispace.API(url = vali_url, username=username, password=password)
            ui.messageBox('Valispace Connected!')
        except Exception as e:
            ui.messageBox(f'Valispace failed to initialize: {str(e)}')

        ui.messageBox(f'{str(vs)}')

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








def search_for_id_by_name(name,valispace):
    """Searches a given valispace for a name.
    If found, returns the ID. If not, returns a list of dictionaries describing the valis


    Args:
        name (str): `name` of valispace .
        valispace (type): Description of parameter `valispace`.

    Returns:
        type: Description of returned object.

    Examples
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>

    """
    valis = valispace.get_vali_list()
    filtered_valis = [v for v in valis if v['name'] == name]
    if len(filtered_valis) == 0:
        raise RuntimeError("No valis of this name found!")
    elif len(filtered_valis) == 1:
        return filtered_valis[0]['id']
    else:
        return filtered_valis
