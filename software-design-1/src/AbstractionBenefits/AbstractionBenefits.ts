// Пример абстракции, который помогает работать с библиотекой в рабочем проекте

type Editor = any;
type Path = any;

type EditorElementTemplate = {
  type: string;
  text?: never;
  children: Array<unknown>;
};

type Normalization<TEditorElement extends EditorElementTemplate> = (
  element: TEditorElement
) => boolean;

const composeNormalizations =
  <TElement extends EditorElementTemplate>(
    ...normalizationsArray: Array<Normalization<TElement>>
  ): Normalization<TElement> =>
  (node) => {
    for (const normalization of normalizationsArray) {
      const isNormalized = normalization(node);

      if (isNormalized) {
        return true;
      }
    }

    return false;
  };

// Пример применения
// const isNodeWasNormalized = composeNormalizations<typeof node>(
//   disabledElementsNormalization,
//   inlineElementsNormalization,
//   editableElementsNormalization,
//   topLevelElementsNormalization
// )(node);
