class ValidationHelper:

    @staticmethod
    def validate_data(requestData={}, rules={}):
        ruleFields = list(rules.keys())
        validationData = {}
        isError = False

        for ruleFiled in ruleFields:
            # required field or not check
            if rules.get(ruleFiled) == "required":
                if requestData.get(ruleFiled) is None:
                    validationData[ruleFiled] = f"{ruleFiled} is required"            
                    isError = True

        return isError, validationData