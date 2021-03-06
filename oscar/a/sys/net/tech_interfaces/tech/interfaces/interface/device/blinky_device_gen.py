


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyContainer
__pychecker__="no-classattr"

from a.infra.basic.return_codes import ReturnCodes
from a.infra.misc.timeout_guard import TimeoutGuard
import a.infra.process.captain
from a.sys.blinky.blinky_container import BlinkyContainer
from a.sys.blinky.trx_phase import TrxPhase
from a.sys.confd.pyconfdlib import pyconfdlib
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value
import copy

from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.device_data_gen import DeviceData



from a.api.yang.modules.tech.common.qwilt_tech_interfaces_types.qwilt_tech_interfaces_types_module_gen import DeviceCountersClearEventType


class BlinkyDevice(BlinkyContainer):
    ourNamespace="http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
    #leaves
    
    ourXmlTagOsName="os-name"
    
    ourXmlTagPciDeviceId="pci-device-id"
    
    ourXmlTagPciVendorId="pci-vendor-id"
    
    ourXmlTagPostUpCommand="post-up-command"
    
    ourXmlTagCountersClearEvent="counters-clear-event"
    
    ourXmlTagPciIndex="pci-index"
    
    ourXmlTagPostInitCommand="post-init-command"
    
    ourXmlTagPostDownCommand="post-down-command"
    

    #descendants
    

    _validationPointId=None
    
    _actionPointId=None
    _actionPointId="tech-interfaces-interface-device-clear-counters-actionpoint"

    
    VALUE_SET_FUNCTOR = 'VALUE_SET_FUNCTOR'
    VALIDATE_TRX_FUNCTOR = 'VALIDATE_TRX_FUNCTOR'
    DO_ACTION_FUNCTOR = 'DO_ACTION_FUNCTOR'

    # Improve performance: Store hashed values of these strings here as well.

    def __init__ (self, logger):
        BlinkyContainer.__init__(self, logger)
        
        self.myValueSetFunctor=None
        self.myCandidateData=None
        self.myRunningData=None
        self.isInDestroy = False
        
        self.validateRegistrationDone = False
        self.actionRegistrationDone=False
        
        
        self.doActionFunctor = None
        

    @classmethod
    def s_create (cls, logger, 
                  
                  
                  
                  interface, 
                  
                  domain):
        __pychecker__="no-argsused"

        logger('s-create-blinkydevice').info('called. domain=%s, _validationPointId=%s, _actionPointId=%s', domain, BlinkyDevice._validationPointId, BlinkyDevice._actionPointId)

        confd_key=KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("device", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(interface);
        confd_key.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("interface", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("interfaces", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        newNode=BlinkyDevice(logger)
        logger("s-create-keypath").info("confd_key=%s", confd_key)
        newNode.setParent(None)
        newNode.setKeyPath(confd_key)
        newNode.setDomain(domain)
        res = newNode.internalInit()
        if (res != ReturnCodes.kOk):
            logger("s-create-internal-init-failed")\
                .error("internalInit() failed. confd_key=%s", confd_key)

        if newNode._validationPointId:
            res = domain.registerValidationPoint(newNode._validationPointId, newNode)
            if (res != ReturnCodes.kOk):
                logger("s-create-register-validation-node--failed")\
                    .error("registerValidationNode(%s) failed",  newNode._validationPointId)
                return None
        newNode.validateRegistrationDone = True
        if newNode._actionPointId:
            res = domain.registerActionPoint(newNode._actionPointId, newNode)
            if (res != ReturnCodes.kOk):
                logger("s-create-register-action-node--failed")\
                    .error("registerActionNode(%s) failed",  newNode._actionPointId)
                return None
        newNode.actionRegistrationDone = True

        return newNode

    

    

    
    def setDoActionFunctor(self, functor):
        if self.myIsActive:
            for logFunc in self._log("set-do-action-functor-active").errorFunc():
                logFunc("illegal when blinky node is active")
        self.doActionFunctor = functor
    

    def trxElementUpdateCandidate(self, trxElement, keyDepth):
        keyPath = trxElement.getKeyPath()
        for logFunc in self._log("trx-element-update-candidate").debug3Func():
            logFunc("trxElementUpdateCandidate(): called, keyPath=%s, keyDepth=%s, trxElement=%s", keyPath, keyDepth, trxElement)
        
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagOsName)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.osName = newValue.asString()
                self.myCandidateData.setHasOsName()
                
            else:
                self.setOsNameDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagPciDeviceId)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.pciDeviceId = newValue.asString()
                self.myCandidateData.setHasPciDeviceId()
                
            else:
                self.setPciDeviceIdDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagPciVendorId)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.pciVendorId = newValue.asString()
                self.myCandidateData.setHasPciVendorId()
                
            else:
                self.setPciVendorIdDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagPostUpCommand)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.postUpCommand = newValue.asString()
                self.myCandidateData.setHasPostUpCommand()
                
            else:
                self.setPostUpCommandDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagCountersClearEvent)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                if not DeviceCountersClearEventType.isValidValue(newValue.asEnum()):
                    self._log("trx-element-update-candidate-illegal-enum-countersclearevent-failed")\
                        .error("illegal enum value %s for countersClearEvent", newValue.asEnum())
                    return ReturnCodes.kGeneralError
                self.myCandidateData.countersClearEvent = DeviceCountersClearEventType.getByValue(newValue.asEnum())
                self.myCandidateData.setHasCountersClearEvent()
                
            else:
                self.setCountersClearEventDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagPciIndex)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.pciIndex = newValue.asUint64()
                self.myCandidateData.setHasPciIndex()
                
            else:
                self.setPciIndexDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagPostInitCommand)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.postInitCommand = newValue.asString()
                self.myCandidateData.setHasPostInitCommand()
                
            else:
                self.setPostInitCommandDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagPostDownCommand)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.postDownCommand = newValue.asString()
                self.myCandidateData.setHasPostDownCommand()
                
            else:
                self.setPostDownCommandDefaultValue(True)
            
        for logFunc in self._log("trx-element-update-candidate-done").debug3Func():
            logFunc("trxElementUpdateCandidate(): After update, candidate is %s", self.myCandidateData)
    
    def getDescendant(self, keyPath, keyDepth_PBR):
        for logFunc in self._log("get-descendant").debug3Func(): logFunc("getDescendant(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        
        for logFunc in self._log("get-descendant-unknown").debug3Func(): logFunc("getDescendant(): unknown, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        return None
    
    @classmethod
    def isKeyPathRegistered (cls, logger, keyPath, keyDepth):
        __pychecker__="no-argsused no-local"
        logger('is-key-path-registered-blinkydevice').debug3('isKeyPathRegistered() called. keyPath=%s, keyDepth=%d, I am: from a.sys.net.tech_interfaces.tech.interfaces.interface.device.blinky_device_gen import BlinkyDevice', keyPath, keyDepth)
        keyPathRegistered = False
        found = False
        
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagOsName)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagPciDeviceId)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagPciVendorId)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagPostUpCommand)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagCountersClearEvent)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagPciIndex)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagPostInitCommand)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagPostDownCommand)):
                keyPathRegistered = True
                found = True
        
        logger('is-key-path-registered-blinkydevice-done').debug3('isKeyPathRegistered() done. registered=%s. keyPath=%s, keyDepth=%d, I am: from a.sys.net.tech_interfaces.tech.interfaces.interface.device.blinky_device_gen import BlinkyDevice', keyPathRegistered, keyPath, keyDepth)
        return keyPathRegistered

    def prepareMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("prepare-my-blinky-node").debug3Func(): logFunc("prepareMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        for logFunc in self._log("prepare-my-blinky-not-found").errorFunc():
            logFunc("prepareMyBlinkyNode(): not found, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        return None
    
    def abortMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("abort-my-blinky-node").debug3Func(): logFunc("abortMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        self.deleteMyBlinkyNode(keyPath, keyDepth)
    
    def deleteMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("delete-my-blinky-node").debug3Func(): logFunc("deleteMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        

    def handleTrxElementCreate(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-create-details").debug3Func():
            logFunc("handleTrxElementCreate(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            pass
        return ReturnCodes.kOk
    
    def handleTrxElementPrepareBlinkyDelete(self, trxElement, keyDepth):
        for logFunc in self._log("handle-trx-element-prepare-blinky-delete-called").debug2Func():
            logFunc("called: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                    trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)

        self.notifyDescendantsPrepareBlinkyDelete()

        # if deleted item is a leaf - clear it in the data
        return self.handleTrxElementPrepareBlinkyValueSet(trxElement, keyDepth)

    def notifyDescendantsPrepareBlinkyDelete(self):
        for logFunc in self._log("notify-descendants-prepare-blinky-delete-called").debug2Func(): logFunc("called")

        self.myDomain.registerNodeToProgressNotification(self)

        pass

        for logFunc in self._log("notify-descendants-prepare-blinky-delete-done").debug2Func(): logFunc("done")

    def handleTrxElementDelete(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-delete-details").debug3Func():
            logFunc("handleTrxElementDelete(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            pass
        # if a leaf is deleted - notify candidate date changed
        return self.notifyWithCandidate(phase)

    

    

    def setValueSetFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-value-set-functor-not-active").errorFunc():
                logFunc("setValueSetFunctor(): is illegal when blinky container is active")
        self.myValueSetFunctor = functor
    
    def activateValueSetFunctor(self, phase, data):
        for logFunc in self._log("activate-value-set-functor").debug3Func():
            logFunc("activateValueSetFunctor(): called, myIsActive=%s, phase=%s, data=%s, candidate=%s, running=%s, functor=%s",
                   self.myIsActive, phase, data, self.myCandidateData, self.myRunningData, self.myValueSetFunctor)
        res = ReturnCodes.kOk
        if (self.myIsActive):
            if (self.myValueSetFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-value-set-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.VALUE_SET_FUNCTOR, phase),
                                            self.getFunctorMildTimeoutForPhase(self.VALUE_SET_FUNCTOR, phase))
                try:
                    res = self.myValueSetFunctor(phase, data)
                except:
                    for logFunc in self._log("activate-value-set-functor-functor-exception").exceptionFunc():
                        logFunc("functor raised an exception. phase=%s, data=%s", phase, data)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myValueSetFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-value-set-functor-failed-prepare").noticeFunc():
                            logFunc("activateValueSetFunctor(): functor failed, phase=%s, data=%s, res=%s",
                                   phase, data, res)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-value-set-functor-failed").errorFunc():
                            logFunc("activateValueSetFunctor(): functor failed, phase=%s, data=%s, res=%s",
                                  phase, data, res)
                    return ReturnCodes.kGeneralError
        return res
    
    def notifyWithCandidate(self, phase):
        for logFunc in self._log("notify-with-candidate").debug3Func(): logFunc("notifyWithCandidate(): called, candidate=%s, phase=%s",
                                                              self.myCandidateData, phase)
        return self.activateValueSetFunctor(phase, self.myCandidateData)
    
    def allocMyCandidate(self):
        for logFunc in self._log("alloc-my-candidate").debug3Func():
            logFunc("called")
        self.myCandidateData = DeviceData()
        
        res = self.setOsNameDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-osname-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setOsNameDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setPciDeviceIdDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-pcideviceid-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setPciDeviceIdDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setPciVendorIdDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-pcivendorid-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setPciVendorIdDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setPostUpCommandDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-postupcommand-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setPostUpCommandDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setCountersClearEventDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-countersclearevent-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setCountersClearEventDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setPciIndexDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-pciindex-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setPciIndexDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setPostInitCommandDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-postinitcommand-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setPostInitCommandDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setPostDownCommandDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-postdowncommand-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setPostDownCommandDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        return ReturnCodes.kOk

    def setOsNameDefaultValue (self, setHas):
        for logFunc in self._log("set-osname-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.osName = ""
            
        if setHas:
            self.myCandidateData.setHasOsName()

        return ReturnCodes.kOk

    def setPciDeviceIdDefaultValue (self, setHas):
        for logFunc in self._log("set-pcideviceid-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.pciDeviceId = ""
            
        if setHas:
            self.myCandidateData.setHasPciDeviceId()

        return ReturnCodes.kOk

    def setPciVendorIdDefaultValue (self, setHas):
        for logFunc in self._log("set-pcivendorid-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.pciVendorId = ""
            
        if setHas:
            self.myCandidateData.setHasPciVendorId()

        return ReturnCodes.kOk

    def setPostUpCommandDefaultValue (self, setHas):
        for logFunc in self._log("set-postupcommand-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.postUpCommand = ""
            
        if setHas:
            self.myCandidateData.setHasPostUpCommand()

        return ReturnCodes.kOk

    def setCountersClearEventDefaultValue (self, setHas):
        for logFunc in self._log("set-countersclearevent-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.countersClearEvent = DeviceCountersClearEventType.kNone
            
        if setHas:
            self.myCandidateData.setHasCountersClearEvent()

        return ReturnCodes.kOk

    def setPciIndexDefaultValue (self, setHas):
        for logFunc in self._log("set-pciindex-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.pciIndex = 0
            
        if setHas:
            self.myCandidateData.setHasPciIndex()

        return ReturnCodes.kOk

    def setPostInitCommandDefaultValue (self, setHas):
        for logFunc in self._log("set-postinitcommand-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.postInitCommand = ""
            
        if setHas:
            self.myCandidateData.setHasPostInitCommand()

        return ReturnCodes.kOk

    def setPostDownCommandDefaultValue (self, setHas):
        for logFunc in self._log("set-postdowncommand-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.postDownCommand = ""
            
        if setHas:
            self.myCandidateData.setHasPostDownCommand()

        return ReturnCodes.kOk

    
    def copyRunningToCandidate(self):
        for logFunc in self._log("copy-running-to-candidate").debug3Func(): logFunc("copyRunningToCandidate(): called, candidate=%s, running=%s",
                                                              self.myCandidateData, self.myRunningData)
        if (self.myCandidateData != None):
            # already coppied - skip
            return

        if (self.myRunningData != None):
            self.myCandidateData = DeviceData()
            self.myCandidateData.copyFrom(self.myRunningData)
            
        else:
            for logFunc in self._log("copy-running-to-candidate-no-running").debug3Func(): logFunc("copyRunningToCandidate(): myRunningData is None")
            res = self.allocMyCandidate()
            if res != ReturnCodes.kOk:
                for logFunc in self._log("copy-running-to-candidate-alloc-my-candidate-failed").errorFunc(): logFunc("copyRunningToCandidate(): myRunningData is None and allocMyCandidate() failed. aborting")
                a.infra.process.processFatal("copyRunningToCandidate(): myRunningData is None and allocMyCandidate() failed")
    
    def deleteMyCandidate(self):
        for logFunc in self._log("delete-my-candidate").debug3Func(): logFunc("deleteMyCandidate(): called, candidate=%s, running=%s",
                                                     self.myCandidateData, self.myRunningData)
        self.myCandidateData = None
    
    def activateCandidate(self):
        phase=TrxPhase(TrxPhase.kCommit, TrxPhase.kBlinky)
        for logFunc in self._log("activate-candidate").debug3Func(): logFunc("activateCandidate(): called, candidate=%s, running=%s, isPhaseDone()=%s",
                                               self.myCandidateData, self.myRunningData, self.myState.isPhaseDone(phase))
        if (self.myState.isPhaseDone(phase)):
            # running config already updated - skip
            return
        self.myRunningData = DeviceData()
        self.myRunningData.copyFrom(self.myCandidateData)
        self.myCandidateData = None
        self.myState.setPhaseDone(phase)
        for logFunc in self._log("activate-candidate-done").debug3Func(): logFunc("activateCandidate(): done, candidate=%s, running=%s, isPhaseDone()=%s",
                                                    self.myCandidateData, self.myRunningData, self.myState.isPhaseDone(phase))

    

    
    def doAction (self, userInfo, actionPoint, actionName, keypath, params, nParams):
        for logFunc in self._log("do-action").debug3Func(): logFunc("called. userInfo=%s, actionPoint=%s, actionName=%s, keypath=%s, paramas=%s, nParams=%s", userInfo, actionPoint, actionName, keypath, params, nParams)
        if self.myIsActive:
            if self.doActionFunctor:
                timeoutGuard = TimeoutGuard(self._log, '%s-do-action-functor-%s' % (keypath, actionPoint), 
                                            self.getFunctorTimeout(self.DO_ACTION_FUNCTOR), 
                                            self.getFunctorMildTimeout(self.DO_ACTION_FUNCTOR))
                try:
                    res = self.doActionFunctor(userInfo, actionPoint, actionName, params, nParams)
                except:
                    for logFunc in self._log("do-action-functor-exception").exceptionFunc():
                        logFunc("functor raised an exception. userInfo=%s, actionPoint=%s, actionName=%s, keypath=%s, paramas=%s, nParams=%s", userInfo, actionPoint, actionName, keypath, params, nParams)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.doActionFunctor.__name__)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log("do-action-functor-failed").errorFunc(): logFunc("functor failed. res=%s, userInfo=%s, actionPoint=%s, actionName=%s, keypath=%s, paramas=%s, nParams=%s", res, userInfo, actionPoint, actionName, keypath, params, nParams)
                    return ReturnCodes.kGeneralError
            else:
                for logFunc in self._log("do-action-functor-unset").debug3Func(): logFunc("no do-action functor set. userInfo=%s, actionPoint=%s, actionName=%s, keypath=%s, paramas=%s, nParams=%s", userInfo, actionPoint, actionName, keypath, params, nParams)
            return ReturnCodes.kOk
        else:
            #TODO (naamas) - add error string
            for logFunc in self._log("d-action-inactive").errorFunc(): logFunc("Blinky node is inactive. userInfo=%s, actionPoint=%s, actionName=%s, keypath=%s, paramas=%s, nParams=%s", userInfo, actionPoint, actionName, keypath, params, nParams)
            return ReturnCodes.kGeneralError
    

    def getRunningCfgData (self):
        if self.myRunningData:
            return copy.copy(self.myRunningData)
        elif self.myCandidateData:
            # running is not yet initialized. getting the candidate that will soon be running
            return copy.copy(self.myCandidateData)
        for logFunc in self._log("get-running-cfg-data").errorFunc(): logFunc("both running and candidate data are none")
        return None

    def getCandidateCfgData (self):
        if self.myCandidateData:
            # when there is no active transaction, there will be no candidate configuration - give the running instead
            if not self.myRunningData:
                for logFunc in self._log("get-candidate-cfg-data").errorFunc(): logFunc("no running and no candidate")
                return None
            return copy.copy(self.myRunningData)
        else:
            # running is not yet initialized. getting the candidate that will soon be running
            return copy.copy(self.myCandidateData)

    def activateSpecific(self):
        for logFunc in self._log("activate-specific").debug3Func(): logFunc("called")
        if self._actionPointId:
            if not self.actionRegistrationDone:
                
                if self.doActionFunctor:
                    res = self.myDomain.registerActionPoint(self._actionPointId, self)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("activate-specitic-register-action-point-failed").errorFunc():
                            logFunc("activateSpecific(): registerActionPoint(%s) failed",  self._actionPointId)
                        return None
                
        return ReturnCodes.kOk

    def handleTrxProgressNotificationSpecific (self, progress):
        for logFunc in self._log("handle-trx-progress-notification-specific").debug3Func(): logFunc("called. progress=%s, isInDestroy=%s", progress, self.isInDestroy)
        if progress.isCommitBlinkyBefore() or progress.isAbortBlinkyBefore():
            if self.isInDestroy:
                if self._validationPointId and self.validateRegistrationDone:
                    res = self.myDomain.unregisterValidationPoint(self._validationPointId, self)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-validation-point-blinkydevice-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterValidationPoint(%s) failed, progress=%s",  self._validationPointId, progress)
                        return ReturnCodes.kGeneralError
                if self._actionPointId and self.actionRegistrationDone:
                    res = self.myDomain.unregisterActionPoint(self, self._actionPointId)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-action-point-blinkydevice-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterActionPoint(%s) failed, progress=%s",  self._actionPointId, progress)
                        return ReturnCodes.kGeneralError
        return ReturnCodes.kOk


    def handleInternalDestroy(self, phase):
        __pychecker__ = 'maxreturns=100 maxlines=1000 maxbranches=100'
        for logFunc in self._log("internal-prepare-destroy-helper").debug3Func(): logFunc("handleInternalDestroy(): called, phase=%s", phase)
        res = ReturnCodes.kOk
        self.isInDestroy = True
        if (phase.getConfdPhase() == TrxPhase.kPrepare):
            self.myDomain.registerNodeToProgressNotification(self)
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                res = self.activateDestroySelfFunctor(phase)
                if (res != ReturnCodes.kOk):
                    for logFunc in self._log("handle-internal-destroy-delete-destroy-self-functor-failed-prepare").noticeFunc():
                        logFunc("handleInternalDestroy(): activateDestroySelfFunctor() failed, res=%s, phase=%s",
                               res, phase)
                    self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    return ReturnCodes.kGeneralError
                
            else:
                for logFunc in self._log("handle-internal-destroy-delete-prepare-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): prepare-illegal-blinky, res=%s, phase=%s",
                           res, phase)
                return ReturnCodes.kGeneralError
        elif (phase.getConfdPhase() == TrxPhase.kCommit):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                res = self.activateDestroySelfFunctor(phase)
                if (res != ReturnCodes.kOk):
                    for logFunc in self._log("handle-internal-destroy-delete-destroy-self-functor-failed-commit").errorFunc():
                        logFunc("handleInternalDestroy(): activateDestroySelfFunctor() failed, res=%s, phase=%s",
                              res, phase)
                    a.infra.process.processFatal("destroy self functor failed in commit")
                    return ReturnCodes.kGeneralError
            else:
                for logFunc in self._log("handle-internal-destroy-delete-commit-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): commit-illegal-blinky, res=%s, phase=%s",
                           res, phase)
                return ReturnCodes.kGeneralError
        elif (phase.getConfdPhase() == TrxPhase.kAbort):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                res = self.activateDestroySelfFunctor(phase)
                if (res != ReturnCodes.kOk):
                    for logFunc in self._log("handle-internal-destroy-activate-destroy-self-functor-failed-abort").errorFunc():
                        logFunc("handleInternalDestroy(): activateDestroySelfFunctor() failed, res=%s, phase=%s",
                              res, phase)
                    a.infra.process.processFatal("destroy self functor failed in abort")
                    return ReturnCodes.kOk
            else:
                for logFunc in self._log("handle-internal-destroy-delete-abort-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): abort-illegal-blinky, res=%s, phase=%s", res, phase)
                return ReturnCodes.kGeneralError
        else:
            for logFunc in self._log("handle-internal-destroy-delete-illegal-confd").noticeFunc():
                logFunc("handleInternalDestroy(): illegal-confd, res=%s, phase=%s", res, phase)
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk
    
"""
Extracted from the below data: 
{
    "node": {
        "dataImportStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.device_data_gen import DeviceData", 
        "moduleYangNamespacePrefix": "qt-if", 
        "validationPoint": null, 
        "yangName": "device", 
        "namespace": "device", 
        "logGroupName": "blinky-device", 
        "className": "BlinkyDevice", 
        "logModuleName": "a-sys-net-tech-interfaces-tech-interfaces-interface-device-blinky-device-gen", 
        "importStatement": "from a.sys.net.tech_interfaces.tech.interfaces.interface.device.blinky_device_gen import BlinkyDevice", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
        "dataClassName": "DeviceData", 
        "actionPoint": "tech-interfaces-interface-device-clear-counters-actionpoint"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "qt", 
            "yangName": "tech", 
            "namespace": "tech", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech", 
            "name": "tech"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "interfaces", 
            "namespace": "interfaces", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "isCurrent": false, 
            "yangName": "interface", 
            "namespace": "interface", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "keyLeaf": {
                "varName": "interface", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "interface"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "device", 
            "namespace": "device", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "device"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "osName", 
            "yangName": "os-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "pciDeviceId", 
            "yangName": "pci-device-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "pciVendorId", 
            "yangName": "pci-vendor-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "postUpCommand", 
            "yangName": "post-up-command", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "countersClearEvent", 
            "yangName": "counters-clear-event", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pciIndex", 
            "yangName": "pci-index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "postInitCommand", 
            "yangName": "post-init-command", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "postDownCommand", 
            "yangName": "post-down-command", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "env": [
        "a", 
        "sys", 
        "net", 
        "tech_interfaces"
    ], 
    "createTime": "2013"
}
"""

