#include "SimApplication/UserRunAction.h"

// LDMX
#include "Event/RootEventWriter.h"
#include "SimPlugins/PluginManager.h"
#include "SimApplication/RootPersistencyManager.h"

using event::RootEventWriter;

namespace sim {

UserRunAction::UserRunAction() {
}

UserRunAction::~UserRunAction() {
}

void UserRunAction::BeginOfRunAction(const G4Run* aRun) {

    std::cout << ">>> Begin Run " << aRun->GetRunID() << " <<<" << std::endl;

    // Open the ROOT writer.
    if (RootPersistencyManager::getInstance()) {
        RootPersistencyManager::getInstance()->Initialize();
    } 

    PluginManager::getInstance().beginRun(aRun);
}

void UserRunAction::EndOfRunAction(const G4Run* aRun) {

    PluginManager::getInstance().endRun(aRun);

    std::cout << ">>> End Run " << aRun->GetRunID() << " <<<" << std::endl;
}

}
