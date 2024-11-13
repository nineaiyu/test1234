import { modelLabelFieldApi } from "@/api/system/field";
import { useI18n } from "vue-i18n";
import { getDefaultAuths } from "@/router/utils";
import { getCurrentInstance, reactive, type Ref, shallowRef } from "vue";
import { handleOperation, type OperationProps } from "@/components/RePlusPage";
import { useRenderIcon } from "@/components/ReIcon/src/hooks";

export function useModelField(tableRef: Ref) {
  const { t } = useI18n();

  const api = reactive(modelLabelFieldApi);

  const auth = reactive({
    sync: false,
    ...getDefaultAuths(getCurrentInstance(), ["sync"])
  });

  const tableBarButtonsProps = shallowRef<OperationProps>({
    buttons: [
      {
        text: t("modelFieldManagement.makeData"),
        code: "sync",
        props: {
          type: "primary",
          plain: true,
          icon: useRenderIcon("ep:money")
        },
        onClick: ({ loading }) => {
          loading.value = true;
          handleOperation({
            t,
            apiReq: api.sync(),
            success() {
              tableRef.value.handleGetData();
            },
            requestEnd() {
              loading.value = false;
            }
          });
        },
        show: auth.sync
      }
    ]
  });

  return {
    t,
    api,
    auth,
    tableBarButtonsProps
  };
}
