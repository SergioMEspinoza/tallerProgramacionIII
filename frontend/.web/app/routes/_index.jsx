import {Fragment,useCallback,useContext,useEffect} from "react"
import {Badge as RadixThemesBadge,Box as RadixThemesBox,Button as RadixThemesButton,Card as RadixThemesCard,Container as RadixThemesContainer,Flex as RadixThemesFlex,Grid as RadixThemesGrid,Heading as RadixThemesHeading,Table as RadixThemesTable,Text as RadixThemesText,TextField as RadixThemesTextField} from "@radix-ui/themes"
import {EventLoopContext,StateContexts} from "$/utils/context"
import {ReflexEvent,isNotNullOrUndefined,isTrue} from "$/utils/state"
import DebounceInput from "react-debounce-input"
import {jsx} from "@emotion/react"




function Badge_e318ddcdf93d13662fb1cd2e137376a7 () {
  const reflex___state____state__frontend___state____inventory_state = useContext(StateContexts.reflex___state____state__frontend___state____inventory_state)



  return (
    jsx(RadixThemesBadge,{color:"green",variant:"surface"},reflex___state____state__frontend___state____inventory_state.rol_usuario_rx_state_)
  )
}


function Button_256cac91ada80353ba46754ee909170a () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_da8924f9c6af54bbc2f6948714b17a35 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.frontend___state____inventory_state.logout", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{color:"red",onClick:on_click_da8924f9c6af54bbc2f6948714b17a35,size:"2",variant:"ghost"},"Cerrar Sesi\u00f3n")
  )
}


function Fragment_52e17f071cf9faaeae74c131dfc2aa45 () {
  const reflex___state____state__frontend___state____inventory_state = useContext(StateContexts.reflex___state____state__frontend___state____inventory_state)



  return (
    jsx(Fragment,{},(((reflex___state____state__frontend___state____inventory_state.rol_usuario_rx_state_?.valueOf?.() === "admin"?.valueOf?.()) || (reflex___state____state__frontend___state____inventory_state.rol_usuario_rx_state_?.valueOf?.() === "medico"?.valueOf?.()))?(jsx(Fragment,{},jsx(RadixThemesGrid,{columns:"3",css:({ ["marginTop"] : "2em", ["marginBottom"] : "2em" }),gap:"4"},jsx(RadixThemesBox,{css:({ ["border"] : "1px solid blue", ["padding"] : "1em", ["borderRadius"] : "lg", ["background"] : "white", ["width"] : "100%" })},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "2em" })},"\ud83d\udce6"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "1.8em", ["fontWeight"] : "bold", ["color"] : "blue" })},"1,240"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "0.9em", ["color"] : "gray" })},"Stock Actual"))),jsx(RadixThemesBox,{css:({ ["border"] : "1px solid red", ["padding"] : "1em", ["borderRadius"] : "lg", ["background"] : "white", ["width"] : "100%" })},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "2em" })},"\u26a0\ufe0f"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "1.8em", ["fontWeight"] : "bold", ["color"] : "red" })},"12"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "0.9em", ["color"] : "gray" })},"Pr\u00f3ximos a Vencer"))),jsx(RadixThemesBox,{css:({ ["border"] : "1px solid green", ["padding"] : "1em", ["borderRadius"] : "lg", ["background"] : "white", ["width"] : "100%" })},jsx(RadixThemesFlex,{align:"center",className:"rx-Stack",direction:"column",gap:"1"},jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "2em" })},"\ud83d\udd04"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "1.8em", ["fontWeight"] : "bold", ["color"] : "green" })},"45"),jsx(RadixThemesText,{as:"p",css:({ ["fontSize"] : "0.9em", ["color"] : "gray" })},"Movimientos Hoy")))))):(jsx(Fragment,{},))))
  )
}


function Debounceinput_5decb56c4208ab469d99094ca8961f70 () {
  const reflex___state____state__frontend___state____inventory_state = useContext(StateContexts.reflex___state____state__frontend___state____inventory_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_837e3b2c7301e8ddc2a43d7866014b33 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.frontend___state____inventory_state.set_nuevo_nombre", ({ ["valor"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_837e3b2c7301e8ddc2a43d7866014b33,placeholder:"Nombre del Insumo",value:(isNotNullOrUndefined(reflex___state____state__frontend___state____inventory_state.nuevo_nombre_rx_state_) ? reflex___state____state__frontend___state____inventory_state.nuevo_nombre_rx_state_ : "")},)
  )
}


function Debounceinput_52bf18bf5a00cde771086c16dc3d5255 () {
  const reflex___state____state__frontend___state____inventory_state = useContext(StateContexts.reflex___state____state__frontend___state____inventory_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_d09f7244f99a20e05e96dfd94b58bd89 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.frontend___state____inventory_state.set_nueva_cantidad", ({ ["valor"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_d09f7244f99a20e05e96dfd94b58bd89,placeholder:"Cantidad",type:"number",value:(isNotNullOrUndefined(reflex___state____state__frontend___state____inventory_state.nueva_cantidad_rx_state_) ? reflex___state____state__frontend___state____inventory_state.nueva_cantidad_rx_state_ : "")},)
  )
}


function Debounceinput_fce47c324f8c121c25f20471752a6ecd () {
  const reflex___state____state__frontend___state____inventory_state = useContext(StateContexts.reflex___state____state__frontend___state____inventory_state)
const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_01b5835944381a91eb65bd468ef9c395 = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.frontend___state____inventory_state.set_nueva_fecha", ({ ["valor"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(DebounceInput,{debounceTimeout:300,element:RadixThemesTextField.Root,onChange:on_change_01b5835944381a91eb65bd468ef9c395,type:"date",value:(isNotNullOrUndefined(reflex___state____state__frontend___state____inventory_state.nueva_fecha_rx_state_) ? reflex___state____state__frontend___state____inventory_state.nueva_fecha_rx_state_ : "")},)
  )
}


function Button_20e75307ddea2279d523be12987c7646 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_5e8a50a44016febec5d3d78f22d9c74d = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.frontend___state____inventory_state.agregar_insumo_local", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{color:"blue",css:({ ["width"] : "100%" }),onClick:on_click_5e8a50a44016febec5d3d78f22d9c74d},"Guardar en Base de Datos")
  )
}


function Fragment_475b304e8c6a72f41d6f98e612753cae () {
  const reflex___state____state__frontend___state____inventory_state = useContext(StateContexts.reflex___state____state__frontend___state____inventory_state)



  return (
    jsx(Fragment,{},((reflex___state____state__frontend___state____inventory_state.rol_usuario_rx_state_?.valueOf?.() === "admin"?.valueOf?.())?(jsx(Fragment,{},jsx(RadixThemesCard,{css:({ ["padding"] : "2em", ["marginBottom"] : "2em", ["width"] : "100%" })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"3"},jsx(RadixThemesHeading,{size:"4"},"Registro de Nuevo Insumo"),jsx(Debounceinput_5decb56c4208ab469d99094ca8961f70,{},),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%" }),direction:"row",gap:"3"},jsx(Debounceinput_52bf18bf5a00cde771086c16dc3d5255,{},),jsx(Debounceinput_fce47c324f8c121c25f20471752a6ecd,{},)),jsx(Button_20e75307ddea2279d523be12987c7646,{},))))):(jsx(Fragment,{},))))
  )
}


function Table__body_28863a8308c45b4a9e519b3f4b2d766a () {
  const reflex___state____state__frontend___state____inventory_state = useContext(StateContexts.reflex___state____state__frontend___state____inventory_state)



  return (
    jsx(RadixThemesTable.Body,{},Array.prototype.map.call(reflex___state____state__frontend___state____inventory_state.lista_insumos_rx_state_ ?? [],((insumo_rx_state_,index_46a960437c994afcabcccffd1d95aeaf)=>(jsx(RadixThemesTable.Row,{key:index_46a960437c994afcabcccffd1d95aeaf},jsx(RadixThemesTable.Cell,{},insumo_rx_state_?.["id"]),jsx(RadixThemesTable.Cell,{},insumo_rx_state_?.["nombre"]),jsx(RadixThemesTable.Cell,{},insumo_rx_state_?.["cantidad"]),jsx(RadixThemesTable.Cell,{},insumo_rx_state_?.["vencimiento"]))))))
  )
}


function Fragment_12cdb68bb4c62f271939354e440280af () {
  const reflex___state____state__frontend___state____inventory_state = useContext(StateContexts.reflex___state____state__frontend___state____inventory_state)



  return (
    jsx(Fragment,{},(((reflex___state____state__frontend___state____inventory_state.rol_usuario_rx_state_?.valueOf?.() === "admin"?.valueOf?.()) || (reflex___state____state__frontend___state____inventory_state.rol_usuario_rx_state_?.valueOf?.() === "enfermera"?.valueOf?.()))?(jsx(Fragment,{},jsx(RadixThemesButton,{color:"orange",css:({ ["marginTop"] : "1em" })},"Registrar Salida de Insumo"))):(jsx(Fragment,{},))))
  )
}


function Textfield__root_2f1ea9f0f8dd1d9c7bd4afeb8313737e () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_1b4971cbce15d62d46e7b42ad668d0bf = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.frontend___state____inventory_state.set_usuario_logueado", ({ ["valor"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesTextField.Root,{css:({ ["background"] : "gray" }),onChange:on_change_1b4971cbce15d62d46e7b42ad668d0bf,placeholder:"Usuario"},)
  )
}


function Textfield__root_1fb3ae260cb6db1cdf95a198adeb9ef0 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_change_0ee655fd0ba0fb271422bc3ace237e5c = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.frontend___state____inventory_state.set_password_input", ({ ["valor"] : _e?.["target"]?.["value"] }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesTextField.Root,{css:({ ["background"] : "gray" }),onChange:on_change_0ee655fd0ba0fb271422bc3ace237e5c,placeholder:"Contrase\u00f1a",type:"password"},)
  )
}


function Button_e0999a977eceec35ed6d929ff636ff6b () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

const on_click_c61cddb9d64711f285b315a22cac115a = useCallback(((_e) => (addEvents([(ReflexEvent("reflex___state____state.frontend___state____inventory_state.login", ({  }), ({  })))], [_e], ({  })))), [addEvents, ReflexEvent])

  return (
    jsx(RadixThemesButton,{color:"teal",css:({ ["width"] : "100px" }),onClick:on_click_c61cddb9d64711f285b315a22cac115a},"Entrar")
  )
}


function Fragment_e889c6583f8d3fe0fa9859e346f92da6 () {
  const reflex___state____state__frontend___state____inventory_state = useContext(StateContexts.reflex___state____state__frontend___state____inventory_state)



  return (
    jsx(Fragment,{},(reflex___state____state__frontend___state____inventory_state.esta_autenticado_rx_state_?(jsx(Fragment,{},jsx(RadixThemesContainer,{css:({ ["padding"] : "16px", ["maxWidth"] : "1000px" }),size:"3"},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["padding"] : "1em", ["borderBottom"] : "1px solid #eaeaea" }),direction:"row",gap:"3"},jsx(RadixThemesHeading,{size:"6"},"Sistema Hemodi\u00e1lisis"),jsx(RadixThemesFlex,{css:({ ["flex"] : 1, ["justifySelf"] : "stretch", ["alignSelf"] : "stretch" })},),jsx(Badge_e318ddcdf93d13662fb1cd2e137376a7,{},),jsx(Button_256cac91ada80353ba46754ee909170a,{},)),jsx(Fragment_52e17f071cf9faaeae74c131dfc2aa45,{},),jsx(Fragment_475b304e8c6a72f41d6f98e612753cae,{},),jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",css:({ ["width"] : "100%", ["marginTop"] : "2em" }),direction:"column",gap:"3"},jsx(RadixThemesHeading,{size:"4"},"Inventario General"),jsx(RadixThemesTable.Root,{css:({ ["width"] : "100%" }),variant:"surface"},jsx(RadixThemesTable.Header,{},jsx(RadixThemesTable.Row,{},jsx(RadixThemesTable.ColumnHeaderCell,{},"ID"),jsx(RadixThemesTable.ColumnHeaderCell,{},"Descripci\u00f3n"),jsx(RadixThemesTable.ColumnHeaderCell,{},"Stock"),jsx(RadixThemesTable.ColumnHeaderCell,{},"Vencimiento"))),jsx(Table__body_28863a8308c45b4a9e519b3f4b2d766a,{},)),jsx(Fragment_12cdb68bb4c62f271939354e440280af,{},))))):(jsx(Fragment,{},jsx(RadixThemesFlex,{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["height"] : "100vh", ["background"] : "#f4f6f8" })},jsx(RadixThemesCard,{css:({ ["padding"] : "2em" })},jsx(RadixThemesFlex,{align:"start",className:"rx-Stack",direction:"column",gap:"4"},jsx(RadixThemesHeading,{as:"h1",color:"blue",size:"9"},"Cl\u00ednica de Hemodi\u00e1lisis SALUVIT S.A."),jsx(RadixThemesHeading,{as:"h2",color:"blue",size:"7"},"SySControl v. 1.1.0"),jsx(Textfield__root_2f1ea9f0f8dd1d9c7bd4afeb8313737e,{},),jsx(Textfield__root_1fb3ae260cb6db1cdf95a198adeb9ef0,{},),jsx(RadixThemesFlex,{css:({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center", ["width"] : "100%" })},jsx(Button_e0999a977eceec35ed6d929ff636ff6b,{},)))))))))
  )
}


export default function Component() {





  return (
    jsx(Fragment,{},jsx(RadixThemesBox,{},jsx(Fragment_e889c6583f8d3fe0fa9859e346f92da6,{},)),jsx("title",{},"SySControl Hemodi\u00e1lisis"),jsx("meta",{content:"favicon.ico",property:"og:image"},))
  )
}