from kraken import plugins
from kraken.core.maths import Xfo, Vec3, Quat

from kraken_examples.mainSrt_component import MainSrtComponentGuide, MainSrtComponentRig

from kraken.core.profiler import Profiler
from kraken.helpers.utility_methods import logHierarchy


Profiler.getInstance().push("mainSrt_build")

mainSrtGuide = MainSrtComponentGuide("mainSrt")
mainSrtGuide.loadData({
                      "name": "mainSrt",
                      "location": "M",
                      "mainSrtXfo": Xfo(tr=Vec3(0.0, 0.0, 0.0)),
                      "mainSrtSize": 3.0
                     })

# Save the main srt guide data for persistence.
saveData = mainSrtGuide.saveData()

mainSrtGuideData = mainSrtGuide.getRigBuildData()

mainSrt = MainSrtComponentRig()
mainSrt.loadData(mainSrtGuideData)

builder = plugins.getBuilder()
builder.build(mainSrt)

Profiler.getInstance().pop()


if __name__ == "__main__":
    print Profiler.getInstance().generateReport()
else:
    logHierarchy(mainSrt)